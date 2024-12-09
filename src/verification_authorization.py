from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.config import settings

AUTH_KEY = settings.AUTH_KEY  # Константное значение для проверки


security = HTTPBearer()


def verify_authentication(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Проверяет, что токен в заголовке Authorization совпадает с AUTH_KEY.
    """
    if credentials.credentials != AUTH_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )
