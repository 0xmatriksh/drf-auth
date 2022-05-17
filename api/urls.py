from .views import ListUsers, ListMessage

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", ListUsers.as_view()),
    path("messages/", ListMessage.as_view(), name="messages"),
    path("login/", obtain_auth_token, name="authtoken"),
]
