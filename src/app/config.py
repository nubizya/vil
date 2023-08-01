"""Module config"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    admin_email: str

    model_config = SettingsConfigDict(env_file="env.local")
