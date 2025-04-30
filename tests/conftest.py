import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def drf_c() -> APIClient:
    u: User = User.objects.create(
        first_name="test_open",
        last_name="test_wheel",
        username="test_openwheel_user",
        email="openwheel_user@google.ca",
        is_active=True
    )
    c: APIClient = APIClient()
    c.force_authenticate(user=u)

    return c

