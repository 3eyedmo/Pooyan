from rest_framework import serializers
from posts_api.models import Post


class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    username = serializers.CharField()


class CommentSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    user = UserSerializer()
    has_reply = serializers.BooleanField()


class CreatePostSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    author = UserSerializer(required=False)
    title = serializers.CharField()
    created = serializers.DateTimeField(required=False)


    
    def create(self, validated_data):
        title = validated_data.get("title")
        request_user = self.context.get("request").user
        post = Post(title=title, author=request_user)
        post.save()
        return post

    
    