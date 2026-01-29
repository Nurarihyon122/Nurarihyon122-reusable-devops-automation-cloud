from fastapi import APIRouter, Depends
from app.core.service_auth import verify_service_token

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/ping")
def ping(_: bool = Depends(verify_service_token)):
    return {"status": "ok", "service": "auth"}
