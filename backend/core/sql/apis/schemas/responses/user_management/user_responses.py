from typing import List
from pydantic import BaseModel


class RegisterResponse(BaseModel):
    access_token: str
    token_type: str


class LoginResponse(BaseModel):
    user_name: str
    email: str
    name: str
    access_token: str
    token_type: str


class UpdateUserResponse(BaseModel):
    user_name: str
    role_name: str
    role_id: str


class UserDetails(BaseModel):
    user_id: int
    password: str
    full_name: str
    user_name: str
    role_name: str
    role_id: int
    email_id: str
