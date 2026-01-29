from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@postgres:5432/postgres"
    JWT_SECRET: str = "dev-secret"
    JWT_ALGORITHM: str = "HS256"

    SERVICE_SHARED_SECRET: str = "internal-secret"

    class Config:
        env_file = ".env"


settings = Settings()
