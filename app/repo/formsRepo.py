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

    def form_update(self, form_id:str, update_data:dict):
        form = self.collection.find_one({"_id":ObjectId(form_id)})
        if not form:
            return False
        result = self.collection.update_one(
            {"_id": ObjectId(form_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0