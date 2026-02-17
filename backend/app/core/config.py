import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "IAAS - Intelligent Academic Advisory System"
    API_V1_STR: str = "/api/v1"
    
    # OpenAI API Key - loaded from .env or environment variable
    OPENAI_API_KEY: str = ""
    # Database
    DATABASE_URL: str = "sqlite:///./data/iaas.db"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
