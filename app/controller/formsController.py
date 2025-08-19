from pymongo import MongoClient

from app.repo.formsRepo import FormsRepository
from app.services.formsService import FormsService


class FormsController:
    def __init__(self):
        client = MongoClient("mongodb+srv://rohikakad:Shree%402020@cluster0.eah3l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client["KMT-react"]
        collections = db["forms"]

        repo = FormsRepository(collections)
        self.ser = FormsService(repo)

    def post_forms(self, form_data):
        return self.ser.post_data(form_data)

    def get_all_forms(self):
        return self.ser.get_all_forms()

    def form_update(self, form_id:str, data):
        return self.ser.form_update(form_id, data)

    def delete_form(self, form_id:str):
        return self.ser.delete_form(form_id)