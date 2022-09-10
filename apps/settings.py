from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = 'E-Commerce API'
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    IS_TEST: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()
