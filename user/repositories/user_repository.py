from user.models import User
from user.serializers import UserSerializer
from rest_framework import serializers


class UserRepository:
    def create_new_user(self, data):
        serializer = UserSerializer(data=data)
        # serializer.validate()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
        # if serializer.validate:
        #     serializer.save()
        #     return serializer.data
        # else:
        #     raise serializers.ValidationError("")

    def get_user_from_firebase_uid(self, uid: str):
        try:
            user = User.objects.get(pk=uid)
            return user
        except User.DoesNotExist:
            return None
