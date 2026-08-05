from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.ai.memory.manager import MemoryManager
from app.ai.service import AIService
from app.database.session import get_db
from app.repositories.memory_repository import MemoryRepository
from app.schemas.chat import ChatRequest
from app.schemas.response import success_response
from app.services.memory_service import MemoryService

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)

ai_service = AIService()


@router.post("")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):

    # Temporary until JWT integration
    user_id = 1

    repository = MemoryRepository(db)
    memory_service = MemoryService(repository)

    conversation = memory_service.get_or_create_conversation(
        request.conversation_id,
        user_id,
    )

    memory_service.save_user_message(
        conversation.id,
        request.message,
    )

    history = memory_service.load_history(
        conversation.id,
    )

    messages = MemoryManager.build_messages(
        history,
        request.message,
    )

    result = ai_service.chat(messages)

    memory_service.save_ai_message(
        conversation.id,
        result["response"],
    )

    return success_response(
        message="Response Generated",
        data={
            "conversation_id": conversation.id,
            **result,
        },
    )
