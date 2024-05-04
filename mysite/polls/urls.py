from django.urls import path

from . import views

urlpatterns = [
    path("current/bdtime", views.home, name="index"),
]