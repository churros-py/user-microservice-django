from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers import TokenSerializer


class Login(TokenObtainPairView):
    serializer_class = TokenSerializer

