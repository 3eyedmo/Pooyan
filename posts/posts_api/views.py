from rest_framework.generics import GenericAPIView
from rest_framework.generics import mixins
from posts_api.serializers.create_post import CreatePostSerializer
from rest_framework.permissions import IsAuthenticated
from posts_api.models import Post

class CreatePostApiView(
    mixins.CreateModelMixin,
    GenericAPIView
):
    permission_classes=[IsAuthenticated]
    serializer_class=CreatePostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListPostApiView(
    mixins.ListModelMixin,
    GenericAPIView
):
    permission_classes=[IsAuthenticated]
    serializer_class=CreatePostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        return Post.objects.filter(author__user_id=self.kwargs.get("user_id"))