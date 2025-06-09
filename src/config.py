from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    
    # Application Settings
    app_name: str = "Task Management API"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # Database Settings
    database_url: str = "postgresql://postgres:postgres@db:5432/postgres"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "postgres"
    postgres_host: str = "db"
    postgres_port: int = 5432
    
    # JWT Settings
    secret_key: str = "your-super-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS Settings
    allowed_origins: str = "http://localhost:3000,http://localhost:8080"
    
    # Legacy setting (keep for compatibility)
    name: str = "Bakhredin"
    
    @property
    def allowed_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.allowed_origins.split(",")]


settings = Settings()
