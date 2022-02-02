from fastapi import APIRouter

from app.api import endpoints as end

routers = APIRouter()

routers.include_router(end.users_router)
