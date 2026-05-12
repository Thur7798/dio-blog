from fastapi import status, APIRouter
from src.schemas.post import PostIn
from src.views.post import PostOut
from src.models.post import posts
from src.db import database

router = APIRouter(prefix="/posts")

@router.get("/", response_model=list[PostOut])
async def read_post():
    query = posts.select()
    return await database.fetch_all(query)
    

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_posts(post : PostIn):
    command = posts.insert().values(
        title=post.title, 
        content = post.content, 
        published_at=post.published_at,
        published=post.published)
    
    last_id=await database.execute(command)
    return {**post.model_dump(), "id": last_id}

@router.put("/{id}", response_model=PostOut)
async def update_post(post: PostIn, id:int):
    
   command = posts.update().values(
       title=post.title, 
        content = post.content, 
        published_at=post.published_at,
        published=post.published
   ).where(posts.c.id==id)
   
   last_id=await database.execute(command)
   return {**post.model_dump(), "id": last_id}

@router.delete("/{id}", response_model=PostOut)
async def delete_post(id: int):
    query = posts.select().where(posts.c.id==id)
    post = await database.fetch_one(query)
    
    command = posts.delete().where(posts.c.id==id)
    await database.execute(command)
    
    return post

@router.get("/{id}", response_model=PostOut)
async def find_post(id:int ):
    query = posts.select().where(posts.c.id==id)
    post = await database.fetch_one(query)
    
    return post