from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from typing import List

from skill_share.authentication import FirebaseAuthentication
from chat.repositories.chat_repository import ChatRepository
from chat.services.chat_service import ChatService

from user.models import User

chatService = ChatService(repository=ChatRepository())


class ChatCreateView(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        data = request.data
        user: User = request.user
        participants = data["participants"]
        participants.append(user.uid)
        data["participants"]=participants
        chat = chatService.create_new_chat(data=data)
        return Response({"message": "success"}, status=status.HTTP_200_OK)
