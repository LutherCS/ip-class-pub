"""
fast jokes api

@author:
@version: 2026.11
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .logic import Joker
from .routes import router

app = FastAPI()
# TODO: Include the router
# TODO: Add CORS middleware
# TODO: Initialize the dataset
