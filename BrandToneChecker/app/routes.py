from fastapi import APIRouter
from app.schemas import BrandCreate, ToneCheck
from app.tone_service import create_brand, check_tone, list_brands

router = APIRouter()

@router.post("/brands")
def add_brand(data: BrandCreate):
    return {
        "brand_id": create_brand(
            data.brand_name,
            data.tone_keywords,
            data.samples
        )
    }

@router.get("/brands")
def brands():
    return list_brands()

@router.post("/check-tone")
def check(data: ToneCheck):
    return check_tone(data.brand_name, data.text)
