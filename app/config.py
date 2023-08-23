from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: Literal["INFO", "DEBUG"]

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    REDIS_HOST: str
    REDIS_PORT: int

    SENTRY_DSN: str

    class Config:
        env_file = ".env"

    def get_database_url(self):
        DATABASE_URL = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return DATABASE_URL

    def get_test_database_url(self):
        TEST_DATABASE_URL = f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
        return TEST_DATABASE_URL

    def get_redis_url(self):
        REDIS_URL = f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"
        return REDIS_URL


settings = Settings()
