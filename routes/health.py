from fastapi import APIRouter

router = APIRouter()

@router.get("/health/status")
async def simple_status():
    return "Ok"

@router.get("/")
async def root_simple_status():
    return "Health Ok"
