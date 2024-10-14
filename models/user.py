from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    role: str
    enabled: bool
    firstname: str
    lastname: str
    appversion: str = "v1"
    