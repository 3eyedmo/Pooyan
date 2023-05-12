from django.urls import path
from . import views

app_name="likes"
urlpatterns = [
    path("like/<str:post_id>/", views.LikeApiView.as_view(), name="like"),
    path("unlike/<str:post_id>/", views.UnlikeApiView.as_view(), name="unlike"),
    path("like_list/<str:post_id>/", views.LikeListApiView.as_view(), name="like_list"),
]
