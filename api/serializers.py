from .models import Message

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer



class UserSerailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True},
            "email": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        token = Token.objects.create(user=user)
        user.save()

        return user


class UserInfoSerailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class MessageSerializer(ModelSerializer):
    created_by = UserInfoSerailizer(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "message", "created_at", "updated_at", "created_by"]

    def save(self, user, **kwargs):
        mes = Message.objects.create(
            message=self.validated_data["message"], created_by=user
        )
        mes.save()

        return mes
