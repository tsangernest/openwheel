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
def test_api_put_nationality_with_name_to_internal_value(drf_c: APIClient):
    # Test setup, so we can then use PUT action with Name, then PUT action with ID
    united_kingdom = Nationality.objects.get(pk=299)
    d = Driver.objects.create(surname="Selmy", date_of_birth="1901-01-01", nationality=united_kingdom)
    # The driver PUT action with nationality in name
    # Everything needs to be the same at the top, except country by name
    driver_payload = {
        "surname": "Selmy",
        "date_of_birth": "1901-01-01",
        "nationality": "United Kingdom",
    }
    # -- begin test --
    # PUT with country text
    response = drf_c.put(path=f"{TEST_PATH}{d.id}/", data=driver_payload, format="json")
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_api_put_nationality_with_id_as_str_to_internal_value(drf_c: APIClient):
    # Test setup, so we can then use PUT action with Name, then PUT action with ID
    united_kingdom = Nationality.objects.get(pk=299)
    d = Driver.objects.create(surname="Selmy", date_of_birth="1901-01-01", nationality=united_kingdom)
    # The driver PUT action with nationality in name
    # Everything needs to be the same at the top, except country by name
    driver_payload = {
        "surname": "Selmy",
        "date_of_birth": "1901-01-01",
        "nationality": "299",
    }
    # -- begin test --
    # PUT with country text
    response = drf_c.put(path=f"{TEST_PATH}{d.id}/", data=driver_payload, format="json")
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.django_db
def test_api_put_nationality_with_id_as_int_to_internal_value(drf_c: APIClient):
    # Test setup, so we can then use PUT action with Name, then PUT action with ID
    united_kingdom = Nationality.objects.get(pk=299)
    d = Driver.objects.create(surname="Selmy", date_of_birth="1901-01-01", nationality=united_kingdom)
    # The driver PUT action with nationality in name
    # Everything needs to be the same at the top, except country by name
    driver_payload = {
        "surname": "Selmy",
        "date_of_birth": "1901-01-01",
        "nationality": 299,
    }
    # -- begin test --
    # PUT with country text
    response = drf_c.put(path=f"{TEST_PATH}{d.id}/", data=driver_payload, format="json")
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_api_get_response_returns_name_of_country(drf_c: APIClient):
    # -- test setup
    driver = Driver.objects.create(surname="Selmy", date_of_birth="1901-01-01", nationality_id=299)
    response = drf_c.get(path=f"{TEST_PATH}{driver.id}/", format="json")
    json_response = response.json()
    assert "United Kingdom" == json_response["nationality"]

