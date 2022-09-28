from datetime import datetime
import json
from typing import Any, Dict, List
import pytest
from freezegun import freeze_time

from django import urls
from django.http.response import HttpResponse
from django.test.client import Client
from django.contrib.auth.hashers import make_password

from rest_framework import status

from api.models import User
from api.utils.seed import seed_down, seed_up


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before test
    seed_up()
    yield
    # Code that will run after test
    seed_down()


@pytest.mark.django_db
@pytest.mark.parametrize("view_name", ["api:login"])
def test_login_with_correct_credentials(view_name, client: Client):
    User.objects.get_or_create(email="test@gmail.com", password=make_password("123"))
    url = urls.reverse(view_name)
    data = {"email": "test@gmail.com", "password": "123"}
    resp: HttpResponse = client.post(url, data)
    response: dict = json.loads(resp.content.decode("utf8"))

    assert resp.status_code == status.HTTP_200_OK
    assert "refresh" in response.keys() and "access" in response.keys()


@pytest.mark.django_db
@pytest.mark.parametrize("view_name", ["api:login"])
def test_login_with_incorrect_credentials(view_name, client: Client):
    User.objects.get_or_create(email="test@gmail.com", password=make_password("123"))
    url = urls.reverse(view_name)
    data = {"email": "test@gmail.com", "password": "wrong password"}
    resp: HttpResponse = client.post(url, data)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize("view_name", ["api:all_users"])
def test_find_all_users(view_name, client: Client):
    url = urls.reverse(view_name)
    resp: HttpResponse = client.get(url)
    response: List[Dict[str, Any]] = json.loads(resp.content.decode("utf8"))

    assert resp.status_code == status.HTTP_200_OK
    assert response[0].get("email") == "test1@test.com"
    assert len(response) == 1
