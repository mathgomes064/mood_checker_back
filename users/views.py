from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"
