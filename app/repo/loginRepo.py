

class LoginRepository:
    def __init__(self,collection):
        self.collection = collection

    def find_user_by_email(self,email:str):
        return self.collection.find_one({"email":email})



