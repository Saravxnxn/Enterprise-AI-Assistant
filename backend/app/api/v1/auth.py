from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.authentication.dependencies import get_current_user
from app.database.session import get_db
from app.repositories import AuthRepository
from app.schemas.auth import LoginRequest
from app.schemas.response import success_response
from app.services import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    repository = AuthRepository(db)

    service = AuthService(repository)

    result = service.login(
        request.username,
        request.password,
    )

    return success_response(
        message="Login Successful",
        data=result,
    )


@router.get("/me")
def me(
    current_user=Depends(get_current_user),
):

    return success_response(
        message="Current User",
        data={
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "full_name": current_user.full_name,
            "status": current_user.status,
        },
    )
