from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = 'E-Commerce API'
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    IS_TEST: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
