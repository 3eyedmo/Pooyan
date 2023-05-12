from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from replies.serializers import ReplySerializer
from replies.models import Reply
from comments.models import Comment
from bson import ObjectId

class RepliesApiView(
    CreateModelMixin,
    ListModelMixin,
    GenericAPIView
):
    serializer_class=ReplySerializer
    permission_classes=(IsAuthenticated, )


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_object(self):
        comment_id = self.kwargs.get("comment_id")
        if len(comment_id) != 24:
            raise APIException("Comment Id Invalid")
        try:
            obj = Comment.objects.get(id=ObjectId(comment_id))
        except Exception as e:
            raise APIException("Comment Does not exists")
        return obj
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "comment": self.get_object()
        })
        return context
    
    def get_queryset(self):
        return Reply.objects.filter(comment_id=self.kwargs.get("comment_id"))