"""Module main"""
from fastapi import FastAPI
from .route.root import root_router

app = FastAPI()


app.include_router(root_router)
