import pytest

from django import urls
from django.http.response import HttpResponse
from django.test.client import Client
from django.contrib.auth.hashers import make_password

from rest_framework import status

from api.models import User


@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['api:login'])
def test_login_with_correct_credentials(view_name, client: Client):
    User.objects.get_or_create(
        email='test@gmail.com',
        password=make_password('123')
    )
    url = urls.reverse(view_name)
    data = {'email': 'test@gmail.com', 'password': '123'}
    resp: HttpResponse = client.post(url, data)

    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.parametrize('view_name', ['api:login'])
def test_login_with_incorrect_credentials(view_name, client: Client):
    User.objects.get_or_create(
        email='test@gmail.com',
        password=make_password('123')
    )
    url = urls.reverse(view_name)
    data = {'email': 'test@gmail.com', 'password': 'wrong password'}
    resp: HttpResponse = client.post(url, data)

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
