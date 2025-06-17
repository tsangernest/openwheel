from datetime import datetime

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient

from app.models import Driver, Nationality
from tests.factories import DriverFactory


TEST_PATH: str = f"/driver/"


@pytest.mark.django_db
def test_driver_get_empty_drivers(drf_c: APIClient):
    assert 0 == Driver.objects.count()
    response = drf_c.get(path=TEST_PATH)
    assert HTTP_200_OK == response.status_code

    json_response = response.json()
    assert 0 == json_response["count"]


@pytest.mark.django_db
def test_get_all_drivers(drf_c: APIClient):
    DriverFactory.create_batch(size=8)
    response = drf_c.get(path=TEST_PATH)
    assert HTTP_200_OK == response.status_code

    json_response = response.json()
    assert 8 == json_response["count"]
    assert 8 == Driver.objects.count()


@pytest.mark.django_db
def test_post_driver_required_fields_zzz(drf_c: APIClient):
    driver_payload: dict = {
        "surname":  "Targaryen",
        "date_of_birth": "01-Jan-2020",
        "nationality": 504,
    }
    response = drf_c.post(path=TEST_PATH, data=driver_payload, format="json")
    assert response.status_code == HTTP_201_CREATED

    json_response = response.json()
    assert json_response["surname"] == driver_payload["surname"]
    assert (
        json_response["nationality"]
        ==
        Nationality
        .objects
        .get(id=driver_payload["nationality"])
        .country
    )
    assert (
        json_response["date_of_birth"]
        ==
        datetime
        .strptime(driver_payload["date_of_birth"], "%d-%b-%Y")
        .strftime("%d-%b-%Y")
    )

    # Test operational
    assert 1 == Driver.objects.count()
    assert 1 == Driver.objects.filter(surname="Targaryen").count()


@pytest.mark.django_db
def test_update_driver_required_fields(drf_c: APIClient):
    dummy_driver = DriverFactory()

    driver_payload: dict = {
        "surname": "Dayne",
        "forename": "Arthur",
        "date_of_birth": "06-Feb-0260",
        "ref": "dayne",
        "nationality": 188,
    }
    response = drf_c.put(path=f"{TEST_PATH}{dummy_driver.id}/", data=driver_payload, format="json")
    assert response.status_code == HTTP_200_OK

    json_response = response.json()
    assert 1 == Driver.objects.count()
    assert json_response["surname"] == driver_payload["surname"]
    assert json_response["forename"] == driver_payload["forename"]
    assert json_response["ref"] == driver_payload["ref"]
    assert (
        json_response["date_of_birth"]
        ==
        datetime
        .strptime(driver_payload["date_of_birth"], "%d-%b-%Y")
        .strftime(format="%d-%b-%Y")
    )


@pytest.mark.django_db
def test_to_internal_value(drf_c: APIClient):
    driver_payload: dict = {
        "surname": "Selmy",
        "date_of_birth": "02-Jun-1236",
        "nationality": "Costa Rica",
    }
    response = drf_c.post(path=TEST_PATH, data=driver_payload, format="json")
    assert response.status_code == HTTP_201_CREATED

    json_response = response.json()
    assert json_response["surname"] == driver_payload["surname"]
    assert (
        json_response["nationality"]
        ==
        Nationality
        .objects
        .get(country=driver_payload["nationality"])
        .country
    )
    assert (
        json_response["date_of_birth"]
        ==
        datetime
        .strptime(driver_payload["date_of_birth"], "%d-%b-%Y")
        .strftime(format="%d-%b-%Y")
    )

