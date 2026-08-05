from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ConversationResponse(BaseModel):

    id: int

    title: str

    user_id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RenameConversationRequest(BaseModel):

    title: str
