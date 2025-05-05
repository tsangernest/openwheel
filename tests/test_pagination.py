from itertools import pairwise
from pprint import pprint

import pytest
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from tests.factories import DriverFactory


@pytest.mark.django_db
def test_sort_by_surname_ascending(drf_c):
    # - test setup -
    DriverFactory.create_batch(10)
    unsorted_response = drf_c.get("/driver/")
    assert HTTP_200_OK == unsorted_response.status_code
    json_unsorted_results = unsorted_response.json()["results"]

    # Grab a list of names, check if it's unsorted (this is what we want)
    unsorted_names: list = [i["surname"] for i in json_unsorted_results]
    print(f"Unsorted:")
    pprint(unsorted_names)
    assert not all(x >= y for x, y in pairwise(unsorted_names))

    # - begin test -
    sorted_response = drf_c.get("/driver/?ordering=surname")
    assert HTTP_200_OK == sorted_response.status_code
    json_sorted_results = sorted_response.json()["results"]
    sorted_names: list = [i["surname"] for i in json_sorted_results]
    assert all(x <= y for x, y in pairwise(sorted_names))
    assert sorted(unsorted_names) == sorted_names
    print(f"\nSORTED:")
    pprint(sorted_names)


@pytest.mark.django_db
def test_sort_by_surname_descending(drf_c):
    # - test setup -
    DriverFactory.create_batch(10)
    unsorted_response = drf_c.get("/driver/")
    assert HTTP_200_OK == unsorted_response.status_code
    json_unsorted_results = unsorted_response.json()["results"]

    # Grab a list of names, check if it's unsorted (this is what we want)
    # The metadata sorts it by id ascending
    unsorted_names: list = [i["forename"] for i in json_unsorted_results]
    print(f"\nUnsorted:")
    pprint(unsorted_names)

    # - begin test -
    sorted_response = drf_c.get("/driver/?ordering=-forename")
    assert HTTP_200_OK == sorted_response.status_code
    json_sorted_results = sorted_response.json()["results"]
    descending_names: list = [i["forename"] for i in json_sorted_results]
    assert sorted(unsorted_names, reverse=True) == descending_names
    print(f"\nSORTED-DESCENDING:")
    pprint(descending_names)


@pytest.mark.django_db
def test_pagination_page_parameter(drf_c):
    # - test setup -
    # Our base pagination paginates with a 'page-size' of 10
    DriverFactory.create_batch(16)

    # - begin test -
    response = drf_c.get("/driver/")
    assert HTTP_200_OK == response.status_code
    json_response = response.json()
    assert 16 == json_response["count"]
    assert 10 == len(json_response["results"])

    # Check 2nd page
    response = drf_c.get("/driver/?page=2")
    assert HTTP_200_OK == response.status_code
    json_response = response.json()
    assert 6 == len(json_response["results"])


@pytest.mark.django_db
def test_pagination_page_size_parameter(drf_c):
    # - test setup -
    DriverFactory.create_batch(8)

    # - begin test -
    response = drf_c.get("/driver/?page-size=3")
    assert HTTP_200_OK == response.status_code
    json_response = response.json()
    assert 8 == json_response["count"]
    assert 3 == len(json_response["results"])

    # test correct number of pages
    response = drf_c.get("/driver/?page-size=3&page=3")
    assert HTTP_200_OK == response.status_code
    json_response = response.json()
    assert 2 == len(json_response["results"])
    assert not json_response["next"]


@pytest.mark.django_db
def test_invalid_parameters(drf_c):
    DriverFactory.create_batch(8)

    response = drf_c.get("/driver/?page=11")
    assert HTTP_404_NOT_FOUND == response.status_code

