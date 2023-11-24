from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import exceptions, generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import (
    LoginSerializers,
    RegisterSerializer,
    UserSerializers,
)


class UserViewSet(viewsets.ModelViewSet):
   
    serializer_class = UserSerializers
    queryset = User.objects.all()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializers

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)[0].key
            message = "user logged in"

            response = {"message": message, "token": token}
            return Response(response)

        else:
            return Response({"message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

