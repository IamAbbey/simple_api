import pytest
from rest_framework.test import APIClient

from api.models import UUIDData


@pytest.fixture(scope="function")
def client():
    return APIClient()


@pytest.fixture(scope="function")
def create_test_data(db):
    test_data = UUIDData.objects.create()
    return test_data
