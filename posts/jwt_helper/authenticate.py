from jwt import InvalidTokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from jwt_helper.models import User


class MongoAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token['user_id']
            username = validated_token['username']
        except KeyError:
            raise InvalidTokenError(_("Token contained no recognizable user identification"))

        user = User(**{
            "user_id": user_id,
            "username": username
        })
        return user