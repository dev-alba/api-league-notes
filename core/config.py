from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, model_validator


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    DB_HOST: str
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: int
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: SecretStr
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env")

    @model_validator(mode="after")
    def verify_environments(self):
        if not self.DATABASE_URL:
            self.DATABASE_URL = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return self


settings = Settings()
