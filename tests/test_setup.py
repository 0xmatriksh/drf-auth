from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
import json


class TestSetUp(APITestCase):
    def setUp(self):
        self.messageurl = reverse("messages")

        self.user = User.objects.get_or_create(
            username="test", email="test@test.com", password="test123"
        )[0]
        self.token = Token.objects.get_or_create(user=self.user)[0].key

        self.message = {
            "message": "Test Msg",
            "created_by": f"{self.user}"
            # {
            #     "username":f'{self.user.username}',
            #     "first_name": f'{self.user.first_name}',
            #     "last_name":f'{self.user.last_name}',
            #     "email":f'{self.user.email}'
            # }
        }

        return super().setUp()
