from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from thoughts import views as thought_view
from moods import views as mood_view

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<str:user_id>/", views.UserDetailView.as_view()),
    path("users/<str:user_id>/thoughts/", thought_view.ThoughtView.as_view()),
    path("users/<str:user_id>/moods/", mood_view.MoodView.as_view()),
]
