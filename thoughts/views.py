from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ThoughtSerializer
from .models import Thought
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticated
# from .permissions import IsObjectOwner
from rest_framework.views import Request


class AllThoughtsView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

    def get_queryset(self):
        self.check_object_permissions(self.request , Request.user)
        queryset = Thought.objects.all()
        return queryset

class ThoughtView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

    def get_queryset(self):
        self.check_object_permissions(self.request , Request.user)
        return Thought.objects.filter(user_id=self.kwargs["user_id"])

    def perform_create(self, serializer):
        self.check_object_permissions(self.request , Request.user)
        return serializer.save(user_id=self.kwargs["user_id"])


class ThoughtDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

    lookup_url_kwarg = "thought_id"

    def perform_update(self, serializer):
        self.check_object_permissions(self.request , Request.user)
        return serializer.save(id=self.kwargs["thought_id"])
    
    def perform_destroy(self, instance):
        self.check_object_permissions(self.request , Request.user)
        return instance.delete()