from fastapi import Header, HTTPException
from app.core.config import settings


def verify_service_token(x_service_token: str = Header(...)):
    if x_service_token != settings.SERVICE_SHARED_SECRET:
        raise HTTPException(status_code=401, detail="Invalid service token")
    return True
