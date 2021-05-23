import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_test_data_list(client):
    url = reverse("test_data_list")
    response = client.get(url)
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["success"]
    assert len(response.data["data"]) == 1


@pytest.mark.django_db
def test_model_str_representation(create_test_data):
    print(create_test_data)
    assert type(str(create_test_data)) == str
