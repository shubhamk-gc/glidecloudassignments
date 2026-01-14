from pydantic import BaseModel
from typing import List

class BrandCreate(BaseModel):
    brand_name: str
    tone_keywords: List[str]
    samples: List[str]

class ToneCheck(BaseModel):
    brand_name: str
    text: str
