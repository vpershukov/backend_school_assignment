import pytest
import requests
import json
import random

#### TEST DATA #####

invalid_data_for_int_fields = [-1, "string", None, 1.1]
invalid_data_for_string_fields = [" ", "", "-", None, 1, -1]
invalid_data_for_birth_date_field = ["", " ", "-", 1, None, "32.12.1986", "26.13.1986", "12.26.1986", "26.12"]
invalid_data_for_relatives_field = [["sdsd"], [""], [None], [1, "qwerty"], [12.2]]

#### TEST DATA #####


# Fixture to get import_id
@pytest.fixture(scope='session')
def get_import_id():
	"""Sending request to first method with valid data to get import_id"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	import_id = response.json()["data"]["import_id"]
	return import_id


#### Tests for the first method: POST /imports ####

def test_import():
	"""Test for the first method with valid data"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 201, "Test failed"


def test_import_with_not_unique_citizen_id():
	"""Test for the first method with not unique citizen_id"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       },
	       {
	           "citizen_id": 1,
	           "town": "Киев",
	           "street": "Киевская",
	           "building": "3",
	           "apartment": 8,
	           "name": "Романова Мария Леонидовна",
	           "birth_date": "23.11.1986",
	           "gender": "female",
	           "relatives": []
	        }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Test failed"


def test_import_without_one_field():
	"""Test for the first method with body without field "town" """
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "There is no town"


def test_import_with_invalid_field_citizen_id():
	"""Test for the first method with invalid field citizen_id"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": random.choice(invalid_data_for_int_fields),
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field citizen_id"


def test_import_with_invalid_field_town():
	"""Test for the first method with invalid field town"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": random.choice(invalid_data_for_string_fields),
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field town"


def test_import_with_invalid_field_street():
	"""Test for the first method with invalid field street"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": random.choice(invalid_data_for_string_fields),
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field street"


def test_import_with_invalid_field_building():
	"""Test for the first method with invalid field building"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": random.choice(invalid_data_for_string_fields),
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field building"


def test_import_with_invalid_field_apartment():
	"""Test for the first method with invalid field apartment"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": random.choice(invalid_data_for_int_fields),
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field apartment"


def test_import_with_invalid_field_name():
	"""Test for the first method with invalid filed name"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": random.choice(invalid_data_for_string_fields),
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid filed name"


def test_import_with_invalid_field_birth_date():
	"""Test for the first method with invalid field birth_date"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": random.choice(invalid_data_for_birth_date_field),
	           "gender": "male",
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field birth_date"


def test_import_with_invalid_field_gender():
	"""Test for the first method with invalid field gender"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": random.choice(invalid_data_for_string_fields),
	           "relatives": []
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field gender"


def test_import_with_invalid_field_relatives():
	"""Test for the first method with invalid field relatives"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": random.choice(invalid_data_for_relatives_field)
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field relatives"


def test_import_with_invalid_field_few_relatives():
	"""Test for the first method with invalid field relatives"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": [2, 1, 4]
	       },
	       {
	           "citizen_id": 2,
	           "town": "Санкт-Петербург",
	           "street": "Невский проспект",
	           "building": "28",
	           "apartment": 1,
	           "name": "Кириллов Кирилл Кириллович",
	           "birth_date": "08.11.1999",
	           "gender": "male",
	           "relatives": [1]
	       },
	       {
	           "citizen_id": 3,
	           "town": "Киев",
	           "street": "Киевская",
	           "building": "3",
	           "apartment": 8,
	           "name": "Романова Мария Леонидовна",
	           "birth_date": "23.11.1986",
	           "gender": "female",
	           "relatives": []
	        }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field relatives"


def test_import_with_extra_field():
	"""Test for the first method with with extra field"""
	url = "http://localhost:5000/imports"
	data_to_send = {
	     "citizens": [
	       {
	           "citizen_id": 1,
	           "town": "Москва",
	           "street": "Льва Толстого",
	           "building": "16к7стр5",
	           "apartment": 7,
	           "name": "Иванов Иван Иванович",
	           "birth_date": "26.12.1986",
	           "gender": "male",
	           "relatives": [],
			   "new_field": "new_field_value"
	       }
	    ]
	}
	response = requests.post(url, json=data_to_send)
	assert response.status_code == 400, "Test failed -- got unknown field"


#### Tests for the second method: PATCH /imports/<int:import_id>/citizens/<int:citizen_id> ####

def test_updates(get_import_id):
	"""Test for the second method with valid data"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"town": "Москва", "street": "Льва Толстого"}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 200, "Test failed"


def test_updates_with_citizen_id_field(get_import_id):
	"""Test for the second method with citizen_id"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"citizen_id": 1, "town": "Москва", "street": "Льва Толстого"}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Body data should not include citizen_id field"


def test_updates_with_invalid_town(get_import_id):
	"""Test for the second method with invalid town"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"town": random.choice(invalid_data_for_string_fields)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field town"


def test_updates_with_invalid_street(get_import_id):
	"""Test for the second method with invalid street"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"street": random.choice(invalid_data_for_string_fields)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field street"


def test_updates_with_invalid_building(get_import_id):
	"""Test for the second method with invalid building"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"building": random.choice(invalid_data_for_string_fields)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field building"


def test_updates_with_invalid_apartment(get_import_id):
	"""Test for the second method with invalid apartment"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"apartment": random.choice(invalid_data_for_int_fields)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field apartment"


def test_updates_with_invalid_name(get_import_id):
	"""Test for the second method with invalid name"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"name": random.choice(invalid_data_for_string_fields)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field name"


def test_updates_with_invalid_birth_date(get_import_id):
	"""Test for the second method with invalid birth_date"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"birth_date": random.choice(invalid_data_for_birth_date_field)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field birth_date"


def test_updates_with_invalid_gender(get_import_id):
	"""Test for the second method with invalid gender"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"gender": random.choice(invalid_data_for_string_fields)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field gender"


def test_updates_with_invalid_relatives(get_import_id):
	"""Test for the second method with invalid relatives"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"relatives": random.choice(invalid_data_for_relatives_field)}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Invalid field relatives"


def test_updates_with_extra_field(get_import_id):
	"""Test for the second method with extra field"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {"town": "Москва", "new_field": "new_field_value"}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Test failed"


def test_updates_with_no_body_data(get_import_id):
	"""Test for the second method with no body data"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/1"
	data_to_send = {}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "Body should contain data"


#### Test for the third method: GET /imports/<int:import_id>/citizens ####

def test_get_import(get_import_id):
	"""Test for the third method with valid data"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens"
	response = requests.get(url)
	assert response.status_code == 200, "Test failed"


#### Test for the fourth method: GET /imports/<int:import_id>/citizens/birthdays ####

def test_get_birthdays(get_import_id):
	"""Test for the fourth method with valid data"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/citizens/birthdays"
	response = requests.get(url)
	assert response.status_code == 200, "Test failed"


#### Test for the fifth method: GET /imports/<int:import_id>/citizens/birthdays ####

def test_get_stat(get_import_id):
	"""Test for the fifth method with valid data"""
	url = "http://localhost:5000/imports/" + str(get_import_id) + "/towns/stat/percentile/age"
	response = requests.get(url)
	assert response.status_code == 200, "Test failed"
