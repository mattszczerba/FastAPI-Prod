from fastapi import FastAPI, Depends
from . import models
from .database import  get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

# CORS policy to allow other hosts to access this api
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
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
    return {"message": "Welcome to my API!!"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts



