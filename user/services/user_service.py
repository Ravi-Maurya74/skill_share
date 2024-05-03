from user.repositories.user_repository import UserRepository

class UserService:
    def __init__(self,repository:UserRepository) -> None:
        self.respository = repository

    def get_user_from_firebase_uid(self,uid:str):
        return self.respository.get_user_from_firebase_uid(uid=uid)
    