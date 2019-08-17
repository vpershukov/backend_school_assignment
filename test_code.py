import requests
import json

def test_import():
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
	assert response.status_code == 201, "test failed"


def test_updates():
	url = "http://localhost:5000/imports/4/citizens/3"
	data_to_send = {"town": "Москва", "street": "Льва Толстого"}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 200, "test failed"


def test_get_import():
	url = "http://localhost:5000/imports/4/citizens"
	response = requests.get(url)
	assert response.status_code == 200, "test failed"


def test_get_birthdays():
	url = "http://localhost:5000/imports/4/citizens/birthdays"
	response = requests.get(url)
	assert response.status_code == 200, "test failed"


def test_get_stat():
	url = "http://localhost:5000/imports/4/towns/stat/percentile/age"
	response = requests.get(url)
	assert response.status_code == 200, "test failed"


def test_invalid_data():
	url = "http://localhost:5000/imports/4/citizens/3"
	data_to_send = {"town1": "Москва", "street": "Льва Толстого"}
	response = requests.patch(url, json=data_to_send)
	assert response.status_code == 400, "test failed"
