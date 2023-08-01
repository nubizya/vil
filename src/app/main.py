"""Module main"""
from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from . import config

app = FastAPI()


@lru_cache()
def get_settings():
    """Function get_settings"""
    return config.Settings()


@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    """Function GET info"""
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
