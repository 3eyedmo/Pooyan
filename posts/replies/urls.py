from django.urls import path
from . import views


app_name="replies"
urlpatterns = [
    path("<str:comment_id>/", views.RepliesApiView.as_view(), name="replies")
]
