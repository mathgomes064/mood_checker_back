from django.urls import path
from . import views

urlpatterns = [
    path("moods/<str:user_id>/", views.MoodView.as_view()),
    path("moods/<str:mood_id>/edit", views.MoodDetailView.as_view()),
]
