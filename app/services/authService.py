from multiprocessing.managers import Token

from dotenv import load_dotenv

from app.models.user import UserLogin
from app.repo.authRepo import AuthRepository
import bcrypt
import jwt
import os
import datetime
import secrets

load_dotenv()
SECRET_KEY = secrets.token_urlsafe(32)


class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def is_user_valid(self,email:str, password:str):
        user = self.repo.find_user_by_email(email, password)
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
            print(user["_id"])
            payload = {
                "user_id": user["_id"],
                "email": user["email"],
                "exp": datetime.datetime.utcnow()+datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return token
        return False
    
    def user_sign_up(self, name:str,email:str,password:str, cpassword:str):
        try:
            return self.repo.create_user(name,email,password, cpassword)
        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception("Failed to create user") from e