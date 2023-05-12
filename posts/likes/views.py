from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.generics import mixins
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from likes.permissions import LikeNotExistsPermission, LikeExistsPermission
from likes.models import Like
from likes.serializers import LikeSerializer
from rest_framework.permissions import IsAuthenticated
from posts_api.models import Post
from bson import ObjectId

class LikeApiView(GenericAPIView):
    permission_classes=[IsAuthenticated , LikeExistsPermission]
    def post(self, request, post_id, *args, **kwargs):
        post = self.get_object()
        self.create_like(post)
        return Response(data={"status": "ok"}, status=status.HTTP_200_OK)
    
    def create_like(self, post):
        like = Like(post_id=str(post.id), user=self.request.user)
        like.save()
        post.like_numbers += 1
        post.save()

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        if len(post_id) != 24:
            raise APIException("Post Id Invalid")
        try:
            obj = Post.objects.get(id=ObjectId(post_id))
        except Exception as e:
            print(e)
            raise APIException("Object Does not exists")
        self.check_object_permissions(self.request, obj)
        return obj
    

class UnlikeApiView(GenericAPIView):
    permission_classes=[IsAuthenticated , LikeNotExistsPermission]
    def post(self, request, post_id, *args, **kwargs):
        post = self.get_object()
        self.make_unlike(post)
        return Response(data={"status": "ok"}, status=status.HTTP_200_OK)
    
    def make_unlike(self, post):
        like = Like.objects.get(post_id=str(post.id), user__user_id=self.request.user.user_id)
        like.delete()
        post.like_numbers -= 1
        post.save()

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        if len(post_id) != 24:
            raise APIException("Post Id Invalid")
        try:
            obj = Post.objects.get(id=ObjectId(post_id))
        except Exception as e:
            print(e)
            raise APIException("Object Does not exists")
        self.check_object_permissions(self.request, obj)
        return obj
    

class LikeListApiView(
    mixins.ListModelMixin,
    GenericAPIView
):
    permission_classes=[IsAuthenticated]
    serializer_class=LikeSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        return Like.objects.filter(post_id=str(ObjectId(self.kwargs.get("post_id"))))