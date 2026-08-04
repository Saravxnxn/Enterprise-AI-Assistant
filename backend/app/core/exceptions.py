from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.schemas.response import error_response


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=422,
        content=error_response(
            message="Validation Error",
            data=exc.errors(),
        ).model_dump(mode="json"),
    )


async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content=error_response(
            message="Internal Server Error",
        ).model_dump(mode="json"),
    )

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=error_response(
            message="Internal Server Error",
        ).model_dump(mode="json"),
    )
    