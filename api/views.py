from django.contrib.auth.hashers import check_password
from django.db.models.query import QuerySet

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from api.models import User


class Login(APIView):
	def post(self, request: Request):
		email: str = request.data.get('email')
		password: str = request.data.get('password')

		user: QuerySet[User] = User.objects.filter(email=email)

		if user and check_password(password, user.get().password):
			return Response(status=status.HTTP_200_OK)
		return Response(status=status.HTTP_401_UNAUTHORIZED)
