from fastapi import HTTPException
from  fastapi import  APIRouter
from starlette.responses import JSONResponse

from app.controller.formsController import FormsController
from app.models.forms import FormData, UpdateFormByID
import json
from bson import ObjectId

router = APIRouter()
controller = FormsController()

@router.post('/add-form')
def add_form_data(data: FormData):
    try:
        result = controller.post_forms(data)
        _id = str(result.inserted_id)
        return {
            "message": "Form submitted",
            "_id": _id
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal server error")

def convert_objected(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

@router.get("/get-all-forms")
def get_all_forms():
    try:
        document = controller.get_all_forms()
        json_doc = json.loads(json.dumps(document, default=convert_objected))
        return JSONResponse(content=json_doc)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/form-update")
def form_update(payload:UpdateFormByID):
    try:
        print("id", payload.id)
        result = controller.form_update(payload.id,payload.update_data)
        if result:
            return {"message": "Form updated successfully", "_id": payload.id}
        else:
            raise ValueError("Forms not found or updated")
    except ValueError as e:
        raise  HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))