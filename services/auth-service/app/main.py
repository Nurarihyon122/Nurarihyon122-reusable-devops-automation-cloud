from fastapi import FastAPI

from app.api import auth
from app.core.init_db import init_db

app = FastAPI(title="Auth Service")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router)

@app.get("/health")
def health():
    return {"status": "ok"}
