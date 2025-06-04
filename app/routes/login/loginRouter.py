from fastapi import APIRouter, HTTPException
from app.models.user import UserLogin
from app.controller.loginController import LoginController


from dotenv import load_dotenv
load_dotenv()
router = APIRouter()
controller = LoginController

@router.post("/login")
def login(user: UserLogin):
    if controller.get_user(user["email"],user["password"]):
        return {"message": "Login success"}
    raise HTTPException(status_code=401, detail="Invalid user")
    

