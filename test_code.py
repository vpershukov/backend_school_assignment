import pytest
import requests
import random

# Test data
invalid_data_for_int_fields = [-1, "string", None, 1.1, ["sdsd"]]
invalid_data_for_string_fields = [" ", "", "-", None, 1, -1, ["sdsd"]] # but not for field name
invalid_data_for_field_name = [None, 1, -1, ["sdsd"], " ", ""]
invalid_data_for_birth_date_field = ["", " ", "-", 1, None, "32.12.1986", "26.13.1986", "26.12", "1993.12.12"]
invalid_data_for_relatives_field = [["sdsd"], [""], [None], [1, "qwerty"], [12.2], 1, None, "qwerty"]

# Fixture to get import_id
@pytest.fixture(scope="session")
def get_import_id():
    """Sending request to first method with valid data to get import_id"""
    url = "http://84.201.163.246:8080/imports"
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
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    import_id = response.json()["data"]["import_id"]
    return import_id


# Tests for the first method: POST /imports
def test_import():
    """Test for the first method with valid data"""
    url = "http://84.201.163.246:8080/imports"
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
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 201, "Test failed. We got: valid data"


def test_import_with_fields_in_another_sequence():
    """Test for the first method with valid data but fields in another sequence"""
    url = "http://84.201.163.246:8080/imports"
    data_to_send = {
        "citizens": [
            {
                "street": "Льва Толстого",
                "relatives": [],
                "birth_date": "26.12.1986",
                "apartment": 7,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "name": "Иванов Иван Иванович",
                "gender": "male",
                "citizen_id": 1,
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 201, "Test failed. We got: valid data but fields in another sequence"


def test_import_with_no_data():
    """Test for the first method with no data"""
    url = "http://84.201.163.246:8080/imports"
    data_to_send = {}
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Body should contain data"


def test_import_with_invalid_type_of_data():
    """Test for the first method with invalid type of data"""
    url = "http://84.201.163.246:8080/imports"
    data_to_send = 12345
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Test failed. We got: invalid type of data"


def test_import_with_not_unique_citizen_id():
    """Test for the first method with not unique citizen_id"""
    url = "http://84.201.163.246:8080/imports"
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
                "relatives": [],
            },
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Not unique citizen_id"


def test_import_without_one_field():
    """Test for the first method with body without field "town" """
    url = "http://84.201.163.246:8080/imports"
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
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "There is no town"


def test_import_with_invalid_field_citizen_id():
    """Test for the first method with invalid field citizen_id"""
    url = "http://84.201.163.246:8080/imports"
    citizen_id = random.choice(invalid_data_for_int_fields)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": citizen_id,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Иван Иванович",
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field citizen_id. We got: {}".format(citizen_id)


def test_import_with_invalid_field_town():
    """Test for the first method with invalid field town"""
    url = "http://84.201.163.246:8080/imports"
    town = random.choice(invalid_data_for_string_fields)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": town,
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Иван Иванович",
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field town. We got: {}".format(town)


def test_import_with_invalid_field_street():
    """Test for the first method with invalid field street"""
    url = "http://84.201.163.246:8080/imports"
    street = random.choice(invalid_data_for_string_fields)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Москва",
                "street": street,
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Иван Иванович",
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field street. We got: {}".format(street)


def test_import_with_invalid_field_building():
    """Test for the first method with invalid field building"""
    url = "http://84.201.163.246:8080/imports"
    building = random.choice(invalid_data_for_string_fields)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": building,
                "apartment": 7,
                "name": "Иванов Иван Иванович",
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field building. We got: {}".format(building)


def test_import_with_invalid_field_apartment():
    """Test for the first method with invalid field apartment"""
    url = "http://84.201.163.246:8080/imports"
    apartment = random.choice(invalid_data_for_int_fields)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": apartment,
                "name": "Иванов Иван Иванович",
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field apartment. We got: {}".format(apartment)


def test_import_with_invalid_field_name():
    """Test for the first method with invalid filed name"""
    url = "http://84.201.163.246:8080/imports"
    name = random.choice(invalid_data_for_field_name)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": name,
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field name. We got: {}".format(name)


def test_import_with_invalid_field_birth_date():
    """Test for the first method with invalid field birth_date"""
    url = "http://84.201.163.246:8080/imports"
    birth_date = random.choice(invalid_data_for_birth_date_field)
    data_to_send = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Иван Иванович",
                "birth_date": birth_date,
                "gender": "male",
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field birth_date. We got: {}".format(birth_date)


def test_import_with_invalid_field_gender():
    """Test for the first method with invalid field gender"""
    url = "http://84.201.163.246:8080/imports"
    gender = random.choice(invalid_data_for_string_fields)
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
                "gender": gender,
                "relatives": [],
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field gender. We got: {}".format(gender)


def test_import_with_invalid_field_relatives():
    """Test for the first method with invalid field relatives"""
    url = "http://84.201.163.246:8080/imports"
    relatives = random.choice(invalid_data_for_relatives_field)
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
                "relatives": relatives,
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field relatives. We got: {}".format(relatives)


def test_import_with_invalid_field_few_relatives():
    """Test for the first method with invalid field relatives"""
    url = "http://84.201.163.246:8080/imports"
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
                "relatives": [2, 1, 4],
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
                "relatives": [1],
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
                "relatives": [],
            },
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field relatives: one way family ties with first citizen"


def test_import_with_extra_field():
    """Test for the first method with with extra field"""
    url = "http://84.201.163.246:8080/imports"
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
                "new_field": "new_field_value",
            }
        ]
    }
    response = requests.post(url, json=data_to_send)
    assert response.status_code == 400, "Unknown field in data_to_send: new_field"


# Tests for the second method: PATCH /imports/<int:import_id>/citizens/<int:citizen_id>
def test_updates(get_import_id):
    """Test for the second method with valid data"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    data_to_send = {"town": "Москва", "street": "Льва Толстого"}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 200, "Test failed"


def test_updates_with_citizen_id_field(get_import_id):
    """Test for the second method with citizen_id"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    data_to_send = {"citizen_id": 1, "town": "Москва", "street": "Льва Толстого"}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Body data should not include citizen_id field"


def test_updates_with_invalid_town(get_import_id):
    """Test for the second method with invalid town"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    town = random.choice(invalid_data_for_string_fields)
    data_to_send = {"town": town}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field town. We got: {}".format(town)


def test_updates_with_invalid_street(get_import_id):
    """Test for the second method with invalid street"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    street = random.choice(invalid_data_for_string_fields)
    data_to_send = {"street": street}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field street. We got: {}".format(street)


def test_updates_with_invalid_building(get_import_id):
    """Test for the second method with invalid building"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    building = random.choice(invalid_data_for_string_fields)
    data_to_send = {"building": building}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field building. We got: {}".format(building)


def test_updates_with_invalid_apartment(get_import_id):
    """Test for the second method with invalid apartment"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    apartment = random.choice(invalid_data_for_int_fields)
    data_to_send = {"apartment": apartment}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field apartment. We got: {}".format(apartment)


def test_updates_with_invalid_name(get_import_id):
    """Test for the second method with invalid name"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    name = random.choice(invalid_data_for_field_name)
    data_to_send = {"name": name}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field name. We got: {}".format(name)


def test_updates_with_invalid_birth_date(get_import_id):
    """Test for the second method with invalid birth_date"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    birth_date = random.choice(invalid_data_for_birth_date_field)
    data_to_send = {"birth_date": birth_date}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field birth_date. We got: {}".format(birth_date)


def test_updates_with_invalid_gender(get_import_id):
    """Test for the second method with invalid gender"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    gender = random.choice(invalid_data_for_string_fields)
    data_to_send = {"gender": gender}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field gender. We got: {}".format(gender)


def test_updates_with_invalid_relatives(get_import_id):
    """Test for the second method with invalid relatives"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    relatives = random.choice(invalid_data_for_relatives_field)
    data_to_send = {"relatives": relatives}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Invalid field relatives. We got: {}".format(relatives)


def test_updates_with_extra_field(get_import_id):
    """Test for the second method with extra field"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    data_to_send = {"town": "Москва", "new_field": "new_field_value"}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Unknown field in data_to_send: new_field"


def test_updates_with_no_body_data(get_import_id):
    """Test for the second method with no body data"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    data_to_send = {}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Body should contain data"


def test_updates_with_invalid_type_of_data(get_import_id):
    """Test for the second method with no body data"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/1"
    data_to_send = 12345
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Test failed. We got: invalid type of data"


def test_updates_with_non_existent_citizen_id(get_import_id):
    """Test for the second method with non existent citizen_id"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/999"
    data_to_send = {"town": "Москва"}
    response = requests.patch(url, json=data_to_send)
    assert response.status_code == 400, "Test failed. We got: non existent citizen_id"


# Tests for the third method: GET /imports/<int:import_id>/citizens
def test_get_import(get_import_id):
    """Test for the third method with valid data"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"


def test_get_import_with_non_existent_import_id():
    """Test for the third method with non existent import id"""
    import_id = 999999
    url = "http://84.201.163.246:8080/imports/" + str(import_id) + "/citizens"
    response = requests.get(url)
    assert response.status_code == 400, "Test failed: non existent import_id"


# Tests for the fourth method: GET /imports/<int:import_id>/citizens/birthdays
def test_get_birthdays(get_import_id):
    """Test for the fourth method with valid data"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/citizens/birthdays"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"


def test_get_birthdays_with_non_existent_import_id():
    """Test for the fourth method with non existent import id"""
    import_id = 999999
    url = "http://84.201.163.246:8080/imports/" + str(import_id) + "/citizens/birthdays"
    response = requests.get(url)
    assert response.status_code == 400, "Test failed: non existent import_id"


# Tests for the fifth method: GET /imports/<int:import_id>/citizens/birthdays
def test_get_stat(get_import_id):
    """Test for the fifth method with valid data"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/towns/stat/percentile/age"
    response = requests.get(url)
    assert response.status_code == 200, "Test failed"


def test_get_stat_with_non_existent_import_id(get_import_id):
    """Test for the fifth method with non existent import id"""
    import_id = 999999
    url = "http://84.201.163.246:8080/imports/" + str(import_id) + "/towns/stat/percentile/age"
    response = requests.get(url)
    assert response.status_code == 400, "Test failed: non existent import_id"


# Test for the request to non existent endpoint
def test_get_data_from_non_existent_endpoint(get_import_id):
    """Test for the request to non existent endpoint"""
    url = "http://84.201.163.246:8080/imports/" + str(get_import_id) + "/some/path"
    response = requests.get(url)
    assert response.status_code == 404, "Test failed"
