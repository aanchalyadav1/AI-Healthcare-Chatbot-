from pydantic import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Health Hackers"
    CORS_ORIGINS: Optional[List[str]] = None
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/healthhackers"
    STORAGE_PATH: str = "./data"
    RISK_THRESHOLD: float = 0.5

    class Config:
        env_file = "../.env.production"

settings = Settings()
