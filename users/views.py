from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(TokenObtainPairView):
    ...

class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"
