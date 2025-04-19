from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.db.models import Q

from .serializer import UserSerializer, LoginSerializer
# Create your views here.

UserModel = get_user_model()

class UserLoginView(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest):
        data = JSONParser().parse(request)
        username = data.get("username")
        password = data.get("password")

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
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserViewSet(viewsets.ModelViewSet):

    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def search(self, request: HttpRequest):
        name = request.GET.get("name")
        company_name = request.GET.get("company_name")
        email = request.GET.get("email")
        number = request.GET.get("number")

        query_object_string = Q()
        if name and name.strip():
            query_object_string &= ( Q(username__icontains=name) | Q(full_name__icontains=name))
        if company_name and company_name.strip():
            query_object_string &= Q(company_name__icontains=company_name)
        if email and email.strip():
            query_object_string &= Q(email__icontains=email)
        if number and number.strip():
            query_object_string &= Q(contact_number__icontains=number)

        users = UserModel.objects.filter(query_object_string)
        if  query_object_string and users.exists():
            users_ser = UserSerializer(users, many=True)
            return Response(data=users_ser.data, status=200)

        return Response(data={"detail": "Users not found!"}, status=404)
