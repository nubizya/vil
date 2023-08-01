"""Module config"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class representing a Setting"""

    app_name: str
    admin_email: str

    model_config = SettingsConfigDict(env_file="env.local")
