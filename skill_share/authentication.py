from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

import firebase_admin
from firebase_admin import credentials

from user.services.user_service import UserService
from user.repositories.user_repository import UserRepository

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./../secrets/secrets/skill-share-67a40-firebase-adminsdk-q4izq-86c5427767.json")
firebase_admin.initialize_app(cred)


class FirebaseAuthentication(BaseAuthentication):
    def __init__(self) -> None:
        self.user_service = UserService(repository=UserRepository())
        super().__init__()

    def authenticate(self, request):
        id_token = request.META.get('HTTP_AUTHORIZATION')

        if not id_token:
            return None

        try:
            decoded_token = firebase_admin.auth.verify_id_token(id_token)
            uid = decoded_token['uid']

            user = self.user_service.get_user_from_firebase_uid(uid=uid)
            return user
            # if user is not None:  
            #     return user
            # else:  # redundant??
            #     raise AuthenticationFailed('User not found')
        except firebase_admin.auth.InvalidIdTokenError:
            raise AuthenticationFailed('Invalid ID token')