import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
ENV = os.getenv("ENV", "dev")

client = MongoClient(MONGO_URL)

db_name = "fastapi_test_db" if ENV == "test" else "fastapi_db"
db = client.get_database(db_name)

users_collection = db.get_collection("users")
