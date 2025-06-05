
from app.models.user import UserLogin
from app.repo.authRepo import AuthRepository
import bcrypt

class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def is_user_valid(self,email:str, password:str):
        user = self.repo.find_user_by_email(email, password)
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
            return True
        return False
    
    def user_sign_up(self, name:str,email:str,password:str, cpassword:str):
        try:
            return self.repo.create_user(name,email,password, cpassword)
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception("Failed to create user") from e

        