from bson import ObjectId, errors
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
        form = self.collection.find({"_id":ObjectId(form_id)})
        if not form:
            return False
        result = self.collection.update_one(
            {"_id": ObjectId(form_id)},
            {"$set": update_data}
        )
        if result.matched_count == 0:
            return "no_found"
        elif result.matched_count == 0:
            return "no_change"
        else:
            return "updated"

    def delete_form(self, form_id):
        try:
            obj_id = ObjectId(form_id)
        except errors.InvalidId:
            return False

        doc = self.collection.find_one({"_id": obj_id})
        if doc:
            result = self.collection.delete_one({"_id": ObjectId(obj_id)})
            return result.deleted_count > 0
        else:
            return False
