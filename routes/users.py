from fastapi import APIRouter, status
from repositories.users import USERS
from requests.newUserRequest import NewUserRequest
from models.user import User

router = APIRouter()

@router.get("/users")
async def list_all():
    return USERS


@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def add_user(new_user:NewUserRequest):
    user = User(**new_user.model_dump())
    USERS.append(user)
    return user

