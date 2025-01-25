from fastapi import APIRouter
from app.models import UserPreference

router = APIRouter()

@router.post("/preferences/")
def set_preferences(preference: UserPreference):
    return {"message": "Preferences saved successfully", "data": preference}
