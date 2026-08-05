from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.conversation_repository import ConversationRepository
from app.schemas.conversation import RenameConversationRequest
from app.schemas.response import success_response
from app.services.conversation_service import ConversationService

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)


@router.get("")
def get_all(
    db: Session = Depends(get_db),
):

    service = ConversationService(ConversationRepository(db))

    conversations = service.get_all()

    return success_response(
        message="Conversation List",
        data=conversations,
    )


@router.get("/{conversation_id}")
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
):

    service = ConversationService(ConversationRepository(db))

    conversation = service.get_conversation(conversation_id)

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    messages = service.get_messages(conversation_id)

    return success_response(
        message="Conversation",
        data=messages,
    )


@router.put("/{conversation_id}")
def rename(
    conversation_id: int,
    request: RenameConversationRequest,
    db: Session = Depends(get_db),
):

    service = ConversationService(ConversationRepository(db))

    conversation = service.get_conversation(conversation_id)

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    conversation = service.rename(
        conversation,
        request.title,
    )

    return success_response(
        message="Conversation Updated",
        data=conversation,
    )


@router.delete("/{conversation_id}")
def delete(
    conversation_id: int,
    db: Session = Depends(get_db),
):

    service = ConversationService(ConversationRepository(db))

    conversation = service.get_conversation(conversation_id)

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    service.delete(conversation)

    return success_response(
        message="Conversation Deleted",
        data=None,
    )
