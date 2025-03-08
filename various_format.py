from pydantic import BaseModel,EmailStr
from datetime import datetime
from pydantic.types import conint


class enter_detail(BaseModel):
    email:EmailStr
    password:str

class response_format(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode=True

class Output_Token(BaseModel):
    token:str
    token_type:str

class Token(BaseModel):
    email:str
    password:str

class post_user_detail(BaseModel):
    id:int
    user_reg_id:int
    content:str
    owner_detail:response_format

    class Config:
        orm_mode=True

class post_user_table_data_custom_purp(BaseModel):
    id:int
    user_reg_id:int
    content:str

    class Config:
        orm_mode=True

class new_response_format_for_join(BaseModel):
    Post:post_user_table_data_custom_purp
    votes:int

    class Config:
        orm_mode=True


class post_table_mandatory_fields(BaseModel):
    content:str


class post_table_update(BaseModel):
    content:str


class vote(BaseModel):
    post_id:int
    direction:conint(le=1)