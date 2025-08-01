from bson import ObjectId
from bson.json_util import dumps, loads


class FormsRepository:
    def __init__(self,collection):
        self.collection = collection

    def post_data(self, form_data):
        return self.collection.insert_one(form_data.dict())

    def get_all_forms(self):
        docs = self.collection.find({})
        docs_json = dumps(docs)
        return loads(docs_json)

    def form_update(self, id:str, update_data:dict):
        result = self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": update_data },
            return_document=True
        )
        return result

