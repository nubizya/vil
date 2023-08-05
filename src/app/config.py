"""Module config"""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class representing a Setting"""

    app_name: str
    admin_email: str

    model_config = SettingsConfigDict(env_file="env.local")


@lru_cache()
def get_settings():
    """Function get_settings"""
    return Settings()
