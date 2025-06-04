

class AuthRepository:
    def __init__(self,collection):
        self.collection = collection

    def find_user_by_email(self,email:str, password:str):
        return self.collection.find_one({"email":email, "password": password})
    
    def create_user(self,name:str,email:str,password:str, cpassword:str):
        existing_user = self.collection.find_one({"email": email})
        if existing_user:
            return None
        result= self.collection.insert_one({"name":name, "email": email, "password": password, "cpassword": cpassword})
        return result.inserted_id