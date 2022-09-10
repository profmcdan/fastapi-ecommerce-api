"""Config of DB"""
import os
from pydantic import Field

from apps.settings import get_settings
from .base import BaseSettings


DB_MODELS = ['apps.user.models', 'apps.business.models', 'apps.product.models', 'aerich.models']


TORTOISE_ORM = {
    "connections": {
         "default": get_settings().DATABASE_URL
    },
    "apps": {
        "models": {
            "models": ['apps.user.models', 'apps.business.models', 'apps.product.models', 'aerich.models'],
            "default_connection": "default",
        }
    },
}


class TortoiseSettings(BaseSettings):
    """Tortoise-ORM settings"""

    db_url: str
    modules: dict
    generate_schemas: bool

    @classmethod
    def generate(cls):
        """Generate Tortoise-ORM settings (with sqlite if tests)"""

        if bool(get_settings().IS_TEST):
            db_url = get_settings().TEST_DATABASE_URL
        else:
            db_url = get_settings().DATABASE_URL
        modules = {"models": DB_MODELS}
        return TortoiseSettings(db_url=db_url, modules=modules, generate_schemas=True)
