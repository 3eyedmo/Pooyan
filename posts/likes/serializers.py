from rest_framework import serializers
from posts_api.serializers.create_post import UserSerializer


class LikeSerializer(serializers.Serializer):
    user = UserSerializer()
    created = serializers.DateTimeField()
    


