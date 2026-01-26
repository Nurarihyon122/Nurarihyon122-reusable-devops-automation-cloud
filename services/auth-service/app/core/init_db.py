from app.core.database import engine
from app.models.base import Base

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database connected and tables created")
