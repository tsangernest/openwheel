from pathlib import Path

import pytest
from django.contrib.auth.models import User
from django.core import management
from pytest_django import DjangoDbBlocker
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker: DjangoDbBlocker):
    with django_db_blocker.unblock():
        fixtures_path = Path("/app/tests/fixtures/")

        fixtures = [f for f in fixtures_path.glob("*.json") if f.is_file()]
        for fixture in fixtures:
            management.call_command("loaddata", fixture, "--format", "json")


@pytest.fixture
def drf_c() -> APIClient:
    u: User = User.objects.create(first_name="test_open",
                                  last_name="test_wheel",
                                  username="test_openwheel_user",
                                  email="openwheel_user@google.ca",
                                  is_active=True)
    c: APIClient = APIClient()
    c.force_authenticate(user=u)

    return c

