from asyncio.windows_events import NULL
from multiprocessing import synchronize
from turtle import title
from typing import Optional
from xmlrpc.client import Boolean
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.params import Body
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}




