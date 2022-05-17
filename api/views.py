from .models import Message
from .serializers import UserSerailizer, MessageSerializer

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle



# Create your views here.
class ListUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerailizer(users, many=True)
        return Response(serializer.data)

    # this is to create the user via api
    def post(self, request, format=None):
        serializer = UserSerailizer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user).key
            data["resonse"] = "successfully registered"
            data["token"] = token
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMessage(APIView):
    permission_classes = [IsAuthenticated]
    scope = "user_hour"
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        tokenstring = request.META["HTTP_AUTHORIZATION"]
        token = str(tokenstring).split(" ")[1]
        user = Token.objects.get(key=token).user

        if serializer.is_valid():
            data = serializer.save(user)

            print(data)

            serializer = MessageSerializer(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
