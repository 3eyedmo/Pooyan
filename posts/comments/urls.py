from django.urls import path
from . import views


app_name="comments"
urlpatterns = [
    path("<str:post_id>/", views.CommentsApiView.as_view(), name="comments"),
    
]
