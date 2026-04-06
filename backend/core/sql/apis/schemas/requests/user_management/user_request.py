from typing import List, Optional
from pydantic import BaseModel, Field


class Register(BaseModel):
    user_name: str = Field(..., description="Unique username")
    password: str
    full_name: str
    email_id: str = Field(None, description="User email Id")
    role_name: str = Field("editor", description="Role to be assigned to the user")
    role_id: int = Field(
        2, description="Role id: 1 for Admin, 2 for Editor, 3 for Viewer"
    )


class Login(BaseModel):
    user_name: str = Field(..., description="Username")
    password: str = Field(..., description="Password")


class UpdateUserRole(BaseModel):
    user_name: str = Field(..., description="Username")
    role_name: str


class ForgotPassword(BaseModel):
    user_name: str
    new_password: str


class UpdatePassword(BaseModel):
    user_name: str
    old_password: str
    new_password: str
