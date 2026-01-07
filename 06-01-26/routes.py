from fastapi import APIRouter, HTTPException
from models import User, UpdateUser
from database import users_collection

from bson import ObjectId

router = APIRouter(prefix="/api")


@router.get("/")
def root():
    return {"message": "FastAPI is running"}

@router.post("/users")
def create_user(user: User):
    result = users_collection.insert_one(user.model_dump())
    return {"id": str(result.inserted_id)}

@router.get("/users")
def get_users():
    users = []
    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

@router.get("/users/{user_id}")
def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])
    return user

@router.put("/users/{user_id}")
def update_user(user_id: str, user: UpdateUser):
    updated = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {k: v for k, v in user.model_dump().items() if v is not None}}
    )

    if updated.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}


@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    deleted = users_collection.delete_one({"_id": ObjectId(user_id)})

    if deleted.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}