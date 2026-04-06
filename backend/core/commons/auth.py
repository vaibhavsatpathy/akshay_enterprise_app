import time
import jwt
import os
from passlib.context import CryptContext
from fastapi import HTTPException, status

# Use Argon2 instead of bcrypt (no 72-byte limit, more secure)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

JWT_SECRET = os.environ.get("secret")
JWT_ALGORITHM = os.environ.get("algorithm")


def signJWT(user_name: str, role_name: str, role_id: int):
    payload = {
        "user_name": user_name,
        "role_name": role_name,
        "role_id": role_id,
        "expires": time.time() + 86400,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception:
        return None


def verify_hash_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password using Argon2 (no length limitations)"""
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        print(f"Password verification error: {e}")
        return False


def encrypt_password(password: str) -> str:
    """Encrypt password using Argon2 (no length limitations)"""
    try:
        return pwd_context.hash(password)
    except Exception as e:
        print(f"Password encryption error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Password encryption failed",
        )


def check_user_authorization(
    user_details: dict,
    allowed_user_role_id: int,
):
    try:
        if user_details.get("role_id") <= allowed_user_role_id:
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient privileges",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Authorization error: {error}")
        raise error
