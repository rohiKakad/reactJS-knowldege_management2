
from app.models.user import UserLogin
from app.repo.loginRepo import LoginRepository

class LoginService:
    def __init__(self, repo: LoginRepository):
        self.repo = repo

    def is_user_valid(self,email:str, password:str):
        user = self.repo.find_user_by_email(email)
        if not user:
            return False
        return user

        
        