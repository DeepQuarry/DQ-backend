from fastapi import APIRouter

from app.api.v1.endpoints import login


router = APIRouter()
# router.include_router(login.router, prefix="/login", tags=["login"])
