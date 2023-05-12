from rest_framework import serializers
from posts_api.serializers.create_post import UserSerializer
from comments.models import Comment



class CommentSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    text = serializers.CharField()
    user = UserSerializer(required=False)
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        text = validated_data.get("text")
        post = self.context.get("post")
        user = self.context.get('request').user

        comment = Comment(text=text, user=user, post_id = str(post.id))
        comment.save()
        return comment

        