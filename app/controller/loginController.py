from pymongo import MongoClient
from app.services.loginService import LoginService
from app.repo.loginRepo import LoginRepository


class LoginController:
    def __init__(self):
        client = MongoClient("mongodb+srv://rohikakad:Shree%402020@cluster0.eah3l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db=client["KMT-react"]
        collection = db["signup"]

        repo = LoginRepository(collection)
        self.ser = LoginService(repo)

    def get_user(self, email: str, password:str):
        return self.ser.is_user_valid(email, password)