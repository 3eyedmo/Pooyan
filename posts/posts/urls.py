
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('api/', include('likes.urls', namespace="likes")),
    path('api/posts/', include("posts_api.urls", namespace="posts_api")),
    path('api/comments/', include("comments.urls", namespace="comments")),
    path('api/replies/', include("replies.urls", namespace="replies"))
]
