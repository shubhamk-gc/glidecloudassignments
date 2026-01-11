from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Brand Tone Checker")
app.include_router(router)
