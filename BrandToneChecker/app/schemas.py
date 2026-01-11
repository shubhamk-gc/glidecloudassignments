from pydantic import BaseModel
from typing import List

class BrandCreate(BaseModel):
    tone_keywords: List[str]
    samples: List[str]

class ToneCheck(BaseModel):
    brand_id: str
    text: str
