from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def simple_hello():
    return "Hello World - V1"

@router.get("/hello-bean")
async def simple_hello_bean():
    return "Hello World Bean - V1"
