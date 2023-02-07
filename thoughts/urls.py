from django.urls import path
from . import views

urlpatterns = [
    path("thoughts/<str:user_id>/", views.ThoughtView.as_view()),
    path("thoughts/<str:thought_id>/edit", views.ThoughtDetailView.as_view()),
]
