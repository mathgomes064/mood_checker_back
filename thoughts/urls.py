from django.urls import path
from . import views

urlpatterns = [
    path("thoughts/", views.ThoughtView.as_view()),
    path("thoughts/<int:pk>/", views.ThoughtDetailView.as_view()),
]
