from rest_framework import serializers
from accounts.models import User
from accounts.utils.validators import validate_passwords

class UserRegisterSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if not 5 < len(username) <= 255:
            raise serializers.ValidationError({
                "username": "username must be between 6 to 255 chars"
            })
        is_valid, msg = validate_passwords(password1, password2)
        if not is_valid:
            raise serializers.ValidationError({
                "passwords": msg
            })
        if User.objects.filter(username=username):
            raise serializers.ValidationError({
                "username": "Username exists."
            })

        return attrs

    def save(self):
        password = self.validated_data.get("password2")
        username = self.validated_data.get("username")
        user = User(username=username)
        user.set_password(password)
        user.save()


