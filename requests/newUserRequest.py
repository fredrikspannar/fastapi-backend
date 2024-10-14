from typing import Optional
from pydantic import BaseModel, Field

class NewUserRequest(BaseModel):
    username: str
    email: str
    role:  Optional[str] = Field(description="App version", default="user")
    enabled: bool
    firstname: str
    lastname: str
    appversion: Optional[str] = Field(default="v1")
    
    
    #id: Optional[str] = Field(description="ID is not needed on create", default=None)
    #title: str = Field(min_length=3)
    #author: str = Field(min_length=2)
    #description: str = Field(min_length=1,max_length=100)
    #rating: int = Field(gt=0, lt=11)
    