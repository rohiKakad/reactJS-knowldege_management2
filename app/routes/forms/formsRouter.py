from http.client import HTTPException
from  fastapi import  APIRouter
from app.controller.formsController import FormsController
from app.models.forms import FormData

router = APIRouter()
controller = FormsController()

@router.post('/add-form')
def add_form_data(data: FormData):
    try:
        result = controller.post_forms(data)
        print("_id"+ result)
        return {
            "message": "Form submitted",
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
