from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.core.init_db import init_db

app = FastAPI(title="Auth Service")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(auth_router)

@app.get("/health")
def health():
    return {"status": "ok"}
