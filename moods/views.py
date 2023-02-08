from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .permissions import IsManager
from thoughts.permissions import IsAuthenticated
from .serializers import MoodSerializer
from .models import Mood
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwner
from rest_framework.views import Request


class AllMoodsView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]
    serializer_class = MoodSerializer

    def get_queryset(self):
        self.check_object_permissions(self.request , Request.user)
        queryset = Mood.objects.all()
        return queryset

class MoodView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()

    def get_queryset(self):
        self.check_object_permissions(self.request , Request.user)
        return Mood.objects.filter(user_id=self.kwargs["user_id"])

    def perform_create(self, serializer):
        self.check_object_permissions(self.request , Request.user)
        return serializer.save(user_id=self.kwargs["user_id"])


class MoodDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MoodSerializer
    queryset = Mood.objects.all()

    lookup_url_kwarg = "mood_id"

    def perform_update(self, serializer):
        self.check_object_permissions(self.request , Request.user)
        return serializer.save(id=self.kwargs["mood_id"])
    
    def perform_destroy(self, instance):
        self.check_object_permissions(self.request , Request.user)
        return instance.delete()
