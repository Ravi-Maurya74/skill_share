from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json

from user.models import User
from user.repositories.user_repository import UserRepository
from user.services.user_service import UserService
from skill_share.authentication import FirebaseAuthentication
from user.serializers import UserSerializer


# Create your views here.

userService = UserService(repository=UserRepository())


class UserCreateView(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        creds = request.auth
        user = request.user
        if user is not None:
            return Response(
                {"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            newUser = userService.create_new_user(data=creds)
            return Response(newUser, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_417_EXPECTATION_FAILED
            )
