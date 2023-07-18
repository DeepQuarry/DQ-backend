from fastapi import APIRouter

from app.api.v1.endpoints import dataset, query

main_router = APIRouter()
main_router.include_router(dataset.router, prefix="/dataset", tags=["datasets"])
main_router.include_router(query.router, prefix="/query", tags=["queries"])
# router.include_router(login.router, prefix="/login", tags=["login"])
