from typing import List

from fastapi import APIRouter, HTTPException
import sqlite3
from .models import User
from .schemas import CreateUser, GetUser, UpdateUser
import ormar

user_router = APIRouter(prefix='/user', tags=["Users"])


@user_router.get("/all", response_model=List[GetUser])
async def get_users():
    return await User.objects.all()


@user_router.post("/create", response_model=GetUser)
async def create_user(user: CreateUser):
    try:
        return await User.objects.create(**user.dict())
    except sqlite3.IntegrityError as err:
        raise HTTPException(status_code=404, detail=str(err))



@user_router.put("/update")
async def update_user(user: UpdateUser):
    user = user.dict()

    user = {k:v for k,v in user.items() if v is not None}
    user_db = await User.objects.get(tid=user["tid"])
    await user_db.update(**user)


@user_router.delete("/delete")
async def delete_user(tid: int):
    user = await User.objects.filter(tid=tid).get()
    await user.delete()
