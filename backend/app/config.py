from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://velix:password@db:5432/velix_crm"
    REDIS_URL: str = "redis://redis:6379/0"
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str
    NETMAP_API_KEY: str
    class Config: env_file = ".env"
settings = Settings()
