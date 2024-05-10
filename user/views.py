from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from user.repositories.user_repository import UserRepository
from user.services.user_service import UserService
from user.serializers import UserSerializer
from skill_share.authentication import FirebaseAuthentication


# Create your views here.

userService = UserService(repository=UserRepository())


class AuthenticateUser(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        creds = request.auth
        user = request.user
        if user is not None:
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        try:
            newUser = userService.create_new_user(data=creds)
            return Response(newUser, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"message": str(e)}, status=status.HTTP_417_EXPECTATION_FAILED
            )
