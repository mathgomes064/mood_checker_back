from django.urls import path
from . import views

urlpatterns = [
    path("thoughts/", views.UserView.as_view()),
    path("thoughts/<int:pk>/", views.UserDetailView.as_view()),
]
