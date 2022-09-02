# -*- coding: utf-8 -*-
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from api.models import User


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["email"] = user.email
        token["is_active"] = user.is_active
        return token


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_joined = serializers.CharField()


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
