from rest_framework import serializers
from posts_api.serializers.create_post import UserSerializer
from replies.models import Reply



class ReplySerializer(serializers.Serializer):
    text = serializers.CharField()
    user = UserSerializer(required=False)
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        text = validated_data.get("text")
        comment = self.context.get("comment")
        user = self.context.get('request').user

        reply = Reply(text=text, user=user, comment_id = str(comment.id))
        reply.save()
        return reply