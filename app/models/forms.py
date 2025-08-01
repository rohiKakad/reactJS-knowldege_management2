from pydantic import BaseModel
from typing import List


class FormData(BaseModel):
    title: str
    desc: str
    assetSpecialist: List[str]
    assetManager: list[str]
    note: str
    isChecked: bool
    status: str
    createdOn: str
    createdBy: str

class UpdateFormByID(BaseModel):
    id:str
    update_data:dict