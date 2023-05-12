from rest_framework import serializers
from accounts.models import User
from jwt_helper.tokens import MongoRefreshToken


class TokenPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    @property
    def get_tokens(self):
        self.is_valid(raise_exception=True)
        username = self.validated_data.get("username")
        password = self.validated_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            raise serializers.ValidationError("username or password is wrong")

        if user.check_password(password):
            refresh = MongoRefreshToken.for_user(user)
            access = refresh.access_token
            tokens = {
                "refresh": str(refresh),
                "access": str(access)
            }
            return tokens

        raise serializers.ValidationError("email or password is wrong")


class AccessTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=4095)

    @property
    def get_access(self):
        self.is_valid(raise_exception=True)
        refresh_token = self.validated_data.get("refresh_token")
        refresh = MongoRefreshToken(refresh_token)
        access_token = refresh.access_token
        return str(access_token)
