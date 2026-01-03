import time
from sqlalchemy.exc import OperationalError
from app.core.database import engine
from app.models.base import Base

def init_db():
    for _ in range(10):  # retry loop (CRITICAL)
        try:
            Base.metadata.create_all(bind=engine)
            return
        except OperationalError:
            time.sleep(2)
    raise RuntimeError("Database not ready")
