from fastapi import APIRouter

from app.core.config import settings
from app.core.constants import STATUS_HEALTHY

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health():

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "database": "connected"
    }