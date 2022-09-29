from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    SIGN_IN_KEY: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn
    PROJECT_NAME: str = "Cachezim"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
