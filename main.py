from fastapi import FastAPI,HTTPException,Depends,status
import models
from db_connection import engine,get_db
import various_format
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from custom_folder import get_users,post,auth
import vote
from fastapi.middleware.cors import CORSMiddleware

# this will create all the models whichever inherited from the base class.
passwd_Context=CryptContext(schemes=["bcrypt"],deprecated="auto")

models.Base.metadata.create_all(bind=engine)  
app=FastAPI()

origin=[
    "https://google.com",
    "https://duckduckgo.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(get_users.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"all right guys!.."}

# for hashing we need a package name called passlib and the algorithm which we will use that is called bcrypt
