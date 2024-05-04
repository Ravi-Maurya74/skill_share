import firebase_admin.firestore
from chat.models import Chat
import firebase_admin


class ChatRepository:
    def create_new_chat_in_firestore(self, data):
        client = firebase_admin.firestore.client()
        chat_collection = client.collection("chats")
        timestamp, document_ref = chat_collection.add(data)
        print(timestamp)
        print(document_ref.id)
        return (document_ref.id)
    
    def create_new_chat_in_database(self,data,document_id):
        return Chat.objects.create(document_id=document_id,**data)
    
    def add_participants_to_chat(self,document_id,participants):
        chat = Chat.objects.get(pk=document_id)
        chat.participants.add(*participants)
        return chat