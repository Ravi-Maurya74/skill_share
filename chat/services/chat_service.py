from chat.models import Chat
from chat.repositories.chat_repository import ChatRepository

class ChatService:
    def __init__(self,repository:ChatRepository) -> None:
        self.repository = repository

    def create_new_chat(self,data:dict):
        document_id = self.repository.create_new_chat_in_firestore(data=data)
        participants = data['participants']
        data.pop('participants')
        chat = self.repository.create_new_chat_in_database(document_id=document_id,data=data)
        return self.repository.add_participants_to_chat(document_id=document_id,participants=participants)