

class FormsRepository:
    def __init__(self,collection):
        self.collection = collection

    def post_data(self, form_data):
        return self.collection.insert_one(form_data.dict())