from db_connection import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__="user_registration"
    id=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class Post(Base):
    __tablename__="user_post"
    id=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    user_reg_id=Column(Integer,ForeignKey("user_registration.id",ondelete="CASCADE"),nullable=False)
    content=Column(String,nullable=False)
    time_zone_created=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_detail=relationship("User")

class Vote(Base):
    __tablename__="votes"
    user_id=Column(Integer,ForeignKey("user_registration.id"),primary_key=True)
    post_id=Column(Integer,ForeignKey("user_post.id"),primary_key=True)
