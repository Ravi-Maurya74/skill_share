from user.models import User

class UserRepository:
    def create_user(self,data):
        return User.objects.create(**data)
    
    def get_user_from_firebase_uid(self,uid:str):
        try:
            user = User.objects.get(pk=uid)
            return user
        except User.DoesNotExist:
            return None