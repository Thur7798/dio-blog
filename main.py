from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.controllers import post
from src.db import *

metadata.create_all(engine) 

@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)



    
