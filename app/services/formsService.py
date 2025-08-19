from app.repo.formsRepo import FormsRepository


class FormsService:
    def __init__(self, repo: FormsRepository):
        self.repo = repo

    def post_data(self,form_data):
        return self.repo.post_data(form_data)

    def get_all_forms(self):
        return self.repo.get_all_forms()

    def form_update(self, form_id:str, data):
        return self.repo.form_update(form_id, data)

    def delete_form(self, form_id:str):
        return self.repo.delete_form(form_id)
