from flask import abort, request
import datetime
import re


# This function is build to validate first method data
def import_validation(citizens):
    citizen_fields = [
        "citizen_id",
        "town",
        "street",
        "building",
        "apartment",
        "name",
        "birth_date",
        "gender",
        "relatives",
    ]
    for citizen in citizens:
        for field in citizen_fields:
            if field not in citizen:
                abort(400)
        for element in citizen:
            if element not in citizen_fields:
                abort(400)

        fields_are_good = all(
            [
                isinstance(citizen["citizen_id"], int),
                isinstance(citizen["town"], str),
                isinstance(citizen["street"], str),
                isinstance(citizen["building"], str),
                isinstance(citizen["apartment"], int),
                isinstance(citizen["name"], str),
                isinstance(citizen["birth_date"], str),
                isinstance(citizen["gender"], str),
                isinstance(citizen["relatives"], list),
            ]
        )
        if not fields_are_good:
            abort(400)

        if citizen["citizen_id"] < 0:
            abort(400)
        if not re.match(r".*\w.*", citizen["town"]):
            abort(400)
        if not re.match(r".*\w.*", citizen["street"]):
            abort(400)
        if not re.match(r".*\w.*", citizen["building"]):
            abort(400)
        if citizen["apartment"] < 0:
            abort(400)
        name = citizen["name"].split()
        if len(name) < 1:
            abort(400)

        birth_date_validation(citizen["birth_date"])

        gender = citizen["gender"]
        if gender not in ("male", "female"):
            abort(400)

        list_relatives = citizen["relatives"]
        unique_relatives = set(citizen["relatives"])
        if len(list_relatives) != len(unique_relatives):
            abort(400)

        relatives_validation(citizens)
        for item in citizen["relatives"]:
            if not isinstance(item, int):
                abort(400)
            if item < 0:
                abort(400)


# This function is build to validate second method data
def update_citizen_validation(citizen):
    citizens_fields = ["town", "street", "building", "apartment", "name", "birth_date", "gender", "relatives"]
    for field in citizen:
        if field not in citizens_fields:
            abort(400)
        if field == "town":
            if not isinstance(citizen["town"], str):
                abort(400)
            if not re.match(r".*\w.*", citizen["town"]):
                abort(400)

        if field == "street":
            if not isinstance(citizen["street"], str):
                abort(400)
            if not re.match(r".*\w.*", citizen["street"]):
                abort(400)

        if field == "building":
            if not isinstance(citizen["building"], str):
                abort(400)
            if not re.match(r".*\w.*", citizen["building"]):
                abort(400)

        if field == "apartment":
            if not isinstance(citizen["apartment"], int):
                abort(400)
            if request.json["apartment"] < 0:
                abort(400)

        if field == "name":
            if not isinstance(citizen["name"], str):
                abort(400)
            name = citizen["name"].split()
            if len(name) < 1:
                abort(400)

        if field == "birth_date":
            if not isinstance(citizen["birth_date"], str):
                abort(400)
            birth_date_validation(citizen["birth_date"])

        if field == "gender":
            if not isinstance(citizen["gender"], str):
                abort(400)
            gender = citizen["gender"]
            if gender not in ("male", "female"):
                abort(400)

        if field == "relatives":
            if not isinstance(citizen["relatives"], list):
                abort(400)


# This function is build to validate birth_date data format
def birth_date_validation(birth_date):
    try:
        datetime.datetime.strptime(birth_date, "%d.%m.%Y")
    except ValueError:
        abort(400)


# This function is build to validate family ties
def relatives_validation(citizens):
    relatives_dict = {citizen["citizen_id"]: set(citizen["relatives"]) for citizen in citizens}
    if len(relatives_dict) != len(citizens):
        abort(400)
    for citizen in citizens:
        for item in citizen["relatives"]:
            if item not in relatives_dict:
                abort(400)
            if citizen["citizen_id"] not in relatives_dict[item]:
                abort(400)
