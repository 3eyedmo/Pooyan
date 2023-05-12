from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers.register import UserRegisterSerializer
from accounts.serializers.tokens import TokenPairSerializer, AccessTokenSerializer


class RegisterUserView(CreateAPIView):
    serializer_class=UserRegisterSerializer


class GetTokenPairView(GenericAPIView):
    serializer_class=TokenPairSerializer
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = TokenPairSerializer(data=data)
        tokens = serializer.get_tokens
        return Response(data={"data": tokens, "status":"ok"}, status=status.HTTP_200_OK)
    

class AccessTokenView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = AccessTokenSerializer(data=data)
        access = serializer.get_access
        return Response(data={"data": access, "status":"ok"}, status=status.HTTP_200_OK)