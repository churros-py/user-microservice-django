# -*- coding: utf-8 -*-
from api.models import User


def seed_up():
    User.objects.create(
        email="test1@test.com",
        password="pbkdf2_sha256$390000$9q1aM6sOug3vDCi4rMTNcL$ctRvli2PKYV7Rk9nldmm4q1xsL1VJZeZTfIhDDowbEA=",  # decript: admin
        is_active=True,
        first_name="Tester",
        last_name="Pleno",
    )


def seed_down():
    User.objects.all().delete()
