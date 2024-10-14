from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repositories.users import USERS, get_user_by_username
from requests.newUserRequest import NewUserRequest
from models.user import User

router = APIRouter()

@router.get("/users")
async def list_all():
    return USERS


@router.post("/user", response_model=User, status_code=status.HTTP_201_CREATED)
async def add_user(new_user:NewUserRequest):
    user = User(**new_user.model_dump())
    
    user.username = user.username.lower() # force lowercase of all usernames
    
    USERS.append(user)
    return user


@router.post("/user/{username}",
            response_model=User,
            responses={
                404: {"message": "User not found", "content": {"application/json": {"example": {"message": "User not found"}}}}
            })
async def get_user(username:str):
    user = get_user_by_username(username)
    
    if user:
        return user
    
    return JSONResponse(content=jsonable_encoder({"message": "User not found"}), status_code=status.HTTP_404_NOT_FOUND)
        
        
