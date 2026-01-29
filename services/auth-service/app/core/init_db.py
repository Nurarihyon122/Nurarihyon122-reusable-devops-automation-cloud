import time
from sqlalchemy.exc import OperationalError
from app.core.database import engine
from app.models.base import Base

def init_db():
    for attempt in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected and tables created")
            return
        except OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(2)

    raise RuntimeError("❌ Database not available after retries")
