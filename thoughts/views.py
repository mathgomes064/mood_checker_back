from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ThoughtSerializer
from .models import Thought
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner


class ThoughtView(ListCreateAPIView):
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()


class ThoughtDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

    lookup_url_kwarg = "user_id"
