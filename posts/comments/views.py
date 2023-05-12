from rest_framework.generics import GenericAPIView
from comments.serializers import CommentSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from posts_api.models import Post
from comments.models import Comment
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from bson import ObjectId

class CommentsApiView(
    CreateModelMixin,
    ListModelMixin,
    GenericAPIView
):
    serializer_class=CommentSerializer
    permission_classes=(IsAuthenticated, )


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        if len(post_id) != 24:
            raise APIException("Post Id Invalid")
        try:
            obj = Post.objects.get(id=ObjectId(post_id))
        except Exception as e:
            raise APIException("Object Does not exists")
        return obj
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "post": self.get_object()
        })
        return context
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs.get("post_id"))
    

