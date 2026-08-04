from fastapi import APIRouter

from app.core.config import settings
from app.core.constants import STATUS_HEALTHY
from app.schemas.response import success_response
router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health():
    #raise Exception("Testing")
    return success_response(
    message="Health Check Successful",
    data={
        "status": STATUS_HEALTHY,
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "database": "connected",
    },
)

