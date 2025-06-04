
from app.models.user import UserLogin
from app.repo.authRepo import AuthRepository

class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def is_user_valid(self,email:str, password:str):
        user = self.repo.find_user_by_email(email, password)
        if not user:
            return False
        return user
    
    def user_sign_up(self, name:str,email:str,password:str, cpassword:str):
        user_id = self.repo.create_user(name,email,password, cpassword)
        if not user_id:
            raise ValueError("User already created")
        return user_id