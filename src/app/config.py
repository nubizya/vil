from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Vil"
    admin_email: str = "admin@vil.com"
