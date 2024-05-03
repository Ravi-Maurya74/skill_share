from user.models import User

class UserRepository:
    def create_user(self,data):
        return User.objects.create(**data)
    
    def get_user_from_firebase_uid(self,uid):
        return User.objects.get(pk=uid)