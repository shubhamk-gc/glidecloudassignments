from fastapi import APIRouter
from app.schemas import BrandCreate, ToneCheck
from app.tone_service import create_brand, check_tone

router = APIRouter()

@router.post("/brands")
def add_brand(data: BrandCreate):
    return {"brand_id": create_brand(data.tone_keywords, data.samples)}

@router.post("/check-tone")
def check(data: ToneCheck):
    return check_tone(data.brand_id, data.text)
