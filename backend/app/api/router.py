from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.chat import router as chat_router
from app.api.v1.conversation import router as conversation_router
from app.api.v1.document import router as document_router
from app.api.v1.health import router as health_router
from app.core.config import settings

api_router = APIRouter(prefix=settings.API_V1_PREFIX)

api_router.include_router(chat_router)
api_router.include_router(auth_router)
api_router.include_router(health_router)
api_router.include_router(conversation_router)
api_router.include_router(document_router)
