import time
from sqlalchemy.exc import OperationalError

from app.core.database import engine, Base

def init_db(retries: int = 10, delay: int = 2):
    for attempt in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected and tables created")
            return
        except OperationalError:
            print(f"⏳ Database not ready, retrying ({attempt+1}/{retries})...")
            time.sleep(delay)

    raise Exception("❌ Database not available after retries")
