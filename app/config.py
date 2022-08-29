from pydantic import BaseSettings, Field, BaseModel

class Settings(BaseSettings):
    database_hostname: str = None
    database_port: str = None
    database_password: str = None
    database_name: str = None
    database_username: str = None
    secret_key: str = None
    algorithm: str = None
    access_token_expire_minutes: int = None

    class Config:
        env_prefix = ""
        env_file = "app/.env"
        env_file_encoding = 'utf-8'


settings = Settings()
