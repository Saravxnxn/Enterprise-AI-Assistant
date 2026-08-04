from datetime import datetime
from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
    timestamp: datetime = datetime.utcnow()


def success_response(
    message: str,
    data: Any = None,
):
    return ApiResponse(
        success=True,
        message=message,
        data=data,
    )


def error_response(
    message: str,
    data: Any = None,
):
    return ApiResponse(
        success=False,
        message=message,
        data=data,
    )