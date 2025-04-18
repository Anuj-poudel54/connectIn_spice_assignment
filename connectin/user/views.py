from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.contrib.auth import authenticate

from .serializer import UserSerializer, LoginSerializer
# Create your views here.

class UserLoginView(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return Response(data={"detail": "Invalid Credentials!"}, status=401)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(data={"detail": "Invalid Credentials!"}, status=401)

        refresh_token = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)

        return Response(data={
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
            'user': user_serializer.data
            }, status=200)



class UserCreateView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
