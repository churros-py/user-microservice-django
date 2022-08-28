from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models import User


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['email'] = user.email
        token['is_active'] = user.is_active
        return token
