from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
    name:str
    email:str
    password:str
    cpassword:str