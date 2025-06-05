import bcrypt

class AuthRepository:
    def __init__(self,collection):
        self.collection = collection

    def find_user_by_email(self,email:str, password:str):
        return self.collection.find_one({"email":email, "password": password})
    
    def create_user(self,name:str,email:str,password:str, cpassword:str):
        existing_user = self.collection.find_one({"email": email})
        if existing_user:
            raise ValueError("User already exists")
        
        if password != cpassword:
            raise ValueError("Password and confirm password does not match")
        
        hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        result= self.collection.insert_one({
            "name":name,
            "email": email,
            "password": hashed_pwd.decode('utf-8'), 
            "cpassword": hashed_pwd.decode('utf-8')
        })
        return result.inserted_id