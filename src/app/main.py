"""Module main"""
from fastapi import FastAPI
from .Routes.root import root_router

app = FastAPI()


app.include_router(root_router)
