from flask import Flask, jsonify, abort, make_response, request
from collections import defaultdict
from pymongo import MongoClient
import numpy as np
import datetime
import re
import validation

app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client.backend_school
imports_collection = db.Imports
IDs_collection = db.IDs

if not IDs_collection.find_one({"id": 0}):
    db.IDs.insert_one({
    "collection" : "Imports",
    "id" : 0})


def insert_doc(doc):
    doc["_id"] = db.IDs.find_and_modify(
        query={"collection": "Imports"},
        update={"$inc": {"id": 1}},
        fields={"id": 1, "_id": 0},
        new=True
    ).get("id")
    doc["import_id"] = doc["_id"]
    try:
        imports_collection.insert_one(doc)
    except errors.DuplicateKeyError as e:
        insert_doc(doc)
    return doc["import_id"]


# First API method
@app.route("/imports", methods=["POST"])
def create_import():
    if not request.json:
        abort(404)
    validation.import_validation(request.json["citizens"])
    new_doc = insert_doc(request.json)

    return jsonify({"data": {"import_id": new_doc}}), 201


# Second API method
@app.route("/imports/<int:import_id>/citizens/<int:citizen_id>", methods=["PATCH"])
def update_citizen(import_id, citizen_id):
    if not request.json:
        abort(400)
    get_import = imports_collection.find_one({"import_id": import_id})
    if not get_import:
        abort(400)
    citizen_id_set = set(map(lambda x: x["citizen_id"], get_import["citizens"]))
    validation.update_citizen_validation(request.json)
    for field in request.json:
        if field == "relatives":
            for item in request.json["relatives"]:
                if not isinstance(item, int):
                    abort(400)
                if item not in citizen_id_set:
                    abort(400)
            current_relatives = imports_collection.find_one({"import_id": import_id, "citizens.citizen_id": citizen_id},
                                                         {"citizens.$": 1})["citizens"][0]["relatives"]
            new_relatives = request.json["relatives"]
            to_delete = list(set(current_relatives) - set(new_relatives))
            to_add = list(set(new_relatives) - set(current_relatives))
            for item in to_delete:
                imports_collection.update_one({"import_id": import_id, "citizens.citizen_id": item},
                                             {"$pull": {"citizens.$.relatives": citizen_id}})
            for item in to_add:
                imports_collection.update_one({"import_id": import_id, "citizens.citizen_id": item},
                                             {"$addToSet": {"citizens.$.relatives": citizen_id}})
    for field in request.json:
        imports_collection.update_one({"import_id": import_id, "citizens.citizen_id": citizen_id},
                                     {"$set": {"citizens.$." + str(field): request.json[field]}}, False, True)
    updated_citizen = imports_collection.find_one({"import_id": import_id, "citizens.citizen_id": citizen_id},
                                         {"citizens.$": 1})["citizens"][0]
    return jsonify({"data": updated_citizen}), 200


# Third API method
@app.route("/imports/<int:import_id>/citizens", methods=["GET"])
def get_citizens(import_id):
    get_import = imports_collection.find_one({"import_id": import_id})
    if not get_import:
        abort(400)
    return jsonify({"data": get_import["citizens"]}), 200


# Fourth API method
@app.route("/imports/<int:import_id>/citizens/birthdays", methods=["GET"]) # TODO: переписать
def get_citizens_and_presents(import_id):
    get_import = imports_collection.find_one({"import_id": import_id})
    if not get_import:
        abort(400)
    citizen_dates = dict()
    month_slice = slice(3, 5)
    for citizen in get_import["citizens"]:
        citizen_dates[str(citizen["citizen_id"])] = int(citizen["birth_date"][month_slice])
    data = dict()
    for i in range(1, 13):
        data[str(i)] = []
    for citizen in get_import["citizens"]:
        citizen_id = citizen["citizen_id"]
        for relative in citizen["relatives"]:
            relative_month = citizen_dates[str(relative)]
            relative_list = data[str(relative_month)]
            if not any(field["citizen_id"] == citizen_id for field in relative_list):
                relative_list.append({"citizen_id": citizen_id, "presents": 1})
            else:
                for i in relative_list:
                    if i["citizen_id"] == citizen_id:
                        i["presents"] += 1
    return jsonify({"data": data}), 200


# Fifth API method
@app.route("/imports/<int:import_id>/towns/stat/percentile/age", methods=["GET"])
def get_statistics(import_id):
    get_import = imports_collection.find_one({"import_id": import_id})
    if not get_import:
        abort(400)
    data = []
    town_list = defaultdict(list)
    today = datetime.datetime.utcnow()
    day_slice = slice(0, 2)
    month_slice = slice(3, 5)
    year_slice = slice(6, 10)
    for citizen in get_import["citizens"]:
        citizen_day = int(citizen["birth_date"][day_slice])
        citizen_month = int(citizen["birth_date"][month_slice])
        citizen_year = int(citizen["birth_date"][year_slice])

        age = today.year - citizen_year
        - ((today.month, today.day) < (citizen_month, citizen_day))
        town_list[citizen["town"]].append(age)

    for town, age in town_list.items():
        a = np.array(age)
        p50 = np.percentile(a, 50, interpolation="linear")
        p75 = np.percentile(a, 75, interpolation="linear")
        p99 = np.percentile(a, 99, interpolation="linear")
        data.append({
        "town": town,
        "p50": "{:.4}".format(p50),
        "p75": "{:.4}".format(p75),
        "p99": "{:.4}".format(p99)
        })
    return jsonify({"data": data}), 200


if __name__ == "__main__":
    app.run(debug=True)
