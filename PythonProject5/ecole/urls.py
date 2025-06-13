from django.urls import path
from . import views

urlpatterns = [
    # Index/page d'accueil
    path("", views.index),
]