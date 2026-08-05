from pydantic import BaseModel


class RenameConversationRequest(BaseModel):
    title: str
