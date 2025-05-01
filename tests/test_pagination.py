import pytest

from tests.factories import DriverFactory


@pytest.mark.django_db
def test_sort_by_name(drf_c):
    dummy_driver = DriverFactory()


    breakpoint()


