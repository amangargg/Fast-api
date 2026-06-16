from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import randrange
from passlib.context import CryptContext

from . import models
from . database import engine
from.routers import post,user,auth,vote

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def root():
    return {"message": "API is running successfully!"}
# origins = ["https://www.google.com","https://www.youtube.com"]
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








