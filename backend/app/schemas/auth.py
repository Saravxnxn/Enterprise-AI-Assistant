from pydantic import BaseModel, ConfigDict, EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    full_name: str
    is_active: bool


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse