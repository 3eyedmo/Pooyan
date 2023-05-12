from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

app_name="accounts"
urlpatterns = [
    path("create_user/", views.RegisterUserView.as_view(), name="create_user"),
    path("token_pair/", views.GetTokenPairView.as_view(), name="token_pair"),
    path("access_token/", views.AccessTokenView.as_view(), name="access_token"),
    path("verify_token/", TokenVerifyView.as_view(), name="verify_token")
]
