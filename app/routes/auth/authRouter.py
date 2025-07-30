from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.responses import JSONResponse

from app.models.user import UserLogin
from app.models.signUpModel import Signup
from app.controller.authController import AuthController

from dotenv import load_dotenv
load_dotenv()

router = APIRouter()
controller = AuthController()
app = FastAPI()

@app.on_event("shutdown")
def shutdown_event():
    if controller.client:
        controller.close_connection()

@router.post("/login")
def login(user: UserLogin):
    token = controller.get_user(user.email, user.password)
    if token:
        return JSONResponse(content=({"access_token": token,"expires_in": 7200, "token_type": "bearer" }))
    raise HTTPException(status_code=401, detail="Invalid email or password")

@router.post("/signup")
def signup(user:Signup):
    try:
        user_id = controller.user_sing_up(user.name, user.email, user.password, user.cpassword)
        return {"message": "User created", "user_id": str(user_id)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")