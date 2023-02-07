from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MoodSerializer
from .models import Mood
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner


class MoodView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()

    def get_queryset(self):
        return Mood.objects.filter(user_id=self.kwargs["user_id"])

    def perform_create(self, serializer):
        return serializer.save(user_id=self.kwargs["user_id"])


class MoodDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()

    lookup_url_kwarg = "mood_id"
