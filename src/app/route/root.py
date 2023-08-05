""" Root Module """
from typing import Annotated
from fastapi import APIRouter, Depends

from src.app.config import get_settings

from .. import config

root_router = APIRouter()


@root_router.get("/")
async def root():
    """Function GET root"""
    return


@root_router.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    """Function GET info"""
    return {"app_name": settings.app_name, "admin_email": settings.admin_email}
