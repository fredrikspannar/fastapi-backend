from typing import List
from models.user import User


# just use an in-memory "database"
USERS:List[User] = []

def get_user_by_username(username:str):
    for stored_user in USERS:
        if stored_user.username.lower() == username.lower():
            return stored_user
        
    return False
