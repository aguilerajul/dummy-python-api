from django.urls import path
from .views import register_action

urlpatterns = [
    path("", register_action, name="register_action"),
]
