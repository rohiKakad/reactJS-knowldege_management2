from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
    name:str
    email:EmailStr
    password:str
    cpassword:str