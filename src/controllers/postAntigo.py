from typing import Annotated, Union 
from fastapi import FastAPI, status, Cookie, Response, Header, APIRouter
from datetime import datetime, UTC
from pydantic import BaseModel
from schemas.post import PostIn
from views.post import PostOut
 
router = APIRouter(prefix="/posts")

fake_db = [
        {"title" : "Criando uma aplicação com Django", "date" : datetime.now(UTC), "published" : True},
        {"title" : "Internacionalizando uma router FastApi", "date" : datetime.now(UTC), "published" : True},
        {"title" : "Internacionalizando uma router Flask", "date" : datetime.now(UTC), "published" : True},
        {"title" : "Internacionalizando uma router Starlett", "date" : datetime.now(UTC), "published" : False}
        ]

    
class Foo(BaseModel):
    bar: str
    message: str    

@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str):
    return {"posts" : [
        {"title" : f"Criando uma aplicação com {framework}", "date" : datetime.now(UTC)},
        {"title" : f"Internacionalizando uma router {framework}", "date" : datetime.now(UTC)}
        ]}
    
@router.get("/", response_model=list[PostOut])
def read_post(response: Response, skip: int = 0, limit: int = len(fake_db), published : bool = True, ads_id : Annotated[str | None, Cookie()] = None,
              user_agent: Annotated[str|None, Header()] = None):
    response.set_cookie(key = 'user', value='thur@gmail.com')
    print(f"Cookie : {ads_id}")
    print(f"User-agent: {user_agent}")
    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post["published"] is published:
            posts.append(post)
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post : PostIn):
    fake_db.routerend(post.model_dump())
    return post

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q" : q} 

@router.get('/foobar/', response_model=Foo)
def foobar() ->Foo:
    return {'bar': 'foo', "message": "hello world"}

    




    
    
