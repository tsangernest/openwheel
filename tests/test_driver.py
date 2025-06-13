from datetime import datetime

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient

from app.models import Driver, Nationality
from tests.factories import DriverFactory


@pytest.mark.django_db
def test_driver_get_empty_drivers(drf_c: APIClient):
    assert 0 == Driver.objects.count()
    response = drf_c.get(path="/driver/")
    assert HTTP_200_OK == response.status_code

    json_response = response.json()
    assert 0 == json_response["count"]


@pytest.mark.django_db
def test_get_all_drivers(drf_c: APIClient):
    DriverFactory.create_batch(size=8)
    response = drf_c.get(path="/driver/")
    assert HTTP_200_OK == response.status_code

    json_response = response.json()
    assert 8 == json_response["count"]
    assert 8 == Driver.objects.count()


@pytest.mark.django_db
def test_post_driver_only_required_fields(drf_c: APIClient):
    driver_payload: dict = {
        "surname":  "Targaryen",
        "date_of_birth": "2025-01-01",
        "nationality": 3,
        "forename": "Daenerys",
    }
    response = drf_c.post(path="/driver/", data=driver_payload, format="json")
    assert HTTP_201_CREATED == response.status_code
    json_response = response.json()
    assert driver_payload["surname"] == json_response["surname"]
    assert driver_payload["forename"] == json_response["forename"]
    assert Nationality.objects.get(id=driver_payload["nationality"]).country == json_response["nationality"]
    assert (
        datetime
        .strptime(driver_payload["date_of_birth"], "%Y-%m-%d")
        .strftime(format="%d-%b-%Y") == json_response["date_of_birth"]
    )

    # Test operational
    assert 1 == Driver.objects.count()
    assert 1 == Driver.objects.filter(surname="Targaryen", forename="Daenerys",).count()

