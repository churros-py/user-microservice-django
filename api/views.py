from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from api.models import User
from api.serializers import CreateUserSerializer, TokenSerializer, UserSerializer


class Login(TokenObtainPairView):
    serializer_class = TokenSerializer


@api_view(["GET", "POST"])
def user(request: Request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user_already_exists = User.objects.filter(
                email=serializer.data.get("email")
            ).first()
            if not user_already_exists:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                {"email": ["This e-mail is already used by another user"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
