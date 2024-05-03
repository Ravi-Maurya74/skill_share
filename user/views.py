from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json

from user.models import User
from user.repositories.user_repository import UserRepository
from user.services.user_service import UserService
from skill_share.authentication import FirebaseAuthentication


# Create your views here.

class UserCreateView(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self,request):
        uid = request.auth
        user = request.user
        return Response(data={
            'uid':uid,
            'user':user,
        },
        status=status.HTTP_200_OK
        )
        