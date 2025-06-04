from pymongo import MongoClient
from app.services.authService import AuthService
from app.repo.authRepo import AuthRepository


class AuthController:
    def __init__(self):
        client = MongoClient("mongodb+srv://rohikakad:Shree%402020@cluster0.eah3l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db=client["KMT-react"]
        collection = db["user"]

        repo = AuthRepository(collection)
        self.ser = AuthService(repo)

    def get_user(self, email: str, password:str):
        return self.ser.is_user_valid(email, password)
    
    def user_sing_up(self, name:str,email:str,password:str, cpassword:str):
        return self.ser.user_sign_up(name,email,password, cpassword)