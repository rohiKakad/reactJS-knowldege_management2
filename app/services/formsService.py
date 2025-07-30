from app.repo.formsRepo import FormsRepository


class FormsService:
    def __init__(self, repo: FormsRepository):
        self.repo = repo

    def post_data(self,form_data):
        return self.repo.post_data(form_data)
