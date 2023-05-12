from django.urls import path
from . import views


app_name="posts_api"
urlpatterns = [
    path("", views.CreatePostApiView.as_view(), name="create_post"),
    path("<str:user_id>/", views.ListPostApiView.as_view(), name="list_posts")
]
