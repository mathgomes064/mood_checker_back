from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ThoughtSerializer
from .models import Thought
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner


class ThoughtView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

    def get_queryset(self):
        return Thought.objects.filter(user_id=self.kwargs["user_id"])

    def perform_create(self, serializer):
        return serializer.save(user_id=self.kwargs["user_id"])


class ThoughtDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

    lookup_url_kwarg = "thought_id"
