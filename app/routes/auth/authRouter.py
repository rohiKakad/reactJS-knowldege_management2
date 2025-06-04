from fastapi import APIRouter, HTTPException
from app.models.user import UserLogin
from app.models.signUpModel import Signup
from app.controller.authController import AuthController

from dotenv import load_dotenv
load_dotenv()

router = APIRouter()
controller = AuthController()


@router.post("/login")
def login(user: UserLogin): 
    if controller.get_user(user.email, user.password):
        return {"message": "Login success"}
    raise HTTPException(status_code=401, detail="Invalid user")

@router.post("/signup")
def signup(user:Signup):
    try:
        user_id = controller.user_sing_up(user.name, user.email, user.password, user.cpassword)
        return {"message": "User created", "user_id": user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")