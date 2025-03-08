from fastapi import FastAPI,APIRouter,Depends,status,HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db_connection import engine,get_db
from typing import List,Optional
# from .. import models,various_format
from models import User,Post,Vote
from various_format import response_format,post_user_detail,new_response_format_for_join
from custom_folder import auth2
from sqlalchemy import func

router=APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.get("/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=response_format)
def give_user_detail(id:int,db:Session=Depends(get_db),get=Depends(auth2.get_current_user)):
    p_f=db.query(User).filter(User.id==id).first()
    if not p_f:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"There is no user for id={id}")
    else:
        p_f.created_at=str(p_f.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        return p_f

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[response_format])
def get_all_users(db:Session=Depends(get_db),get=Depends(auth2.get_current_user)):
    all_records=db.query(User).all()
    for i in all_records:
        print("created at:- ",i.created_at)
        i.created_at=str(i.created_at.strftime("%Y-%m-%d %H:%M:%S"))
    return all_records

@router.delete("/delete/{id}",status_code=status.HTTP_200_OK)
def delete_user(id:int,db:Session=Depends(get_db),get=Depends(auth2.get_current_user)):
    record=db.query(User).filter(User.id==id)
    # record=record.first()
    original_record=record.first()
    if not original_record:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"The user is not found in the database for id ={id}")
    else:
        record.delete(synchronize_session=False)
        db.commit()
        print(jsonable_encoder(original_record))
        return {"data":jsonable_encoder(original_record)}

@router.get("/post_table/{id}",status_code=status.HTTP_200_OK,response_model=post_user_detail)
def get_user_detail_from_post_table(id:int,db:Session=Depends(get_db),get=Depends(auth2.get_current_user)):
    record=db.query(Post).filter(Post.id==id).first()
    if record:
        return record
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"there is no user who's id is {id} in the database.")
    

@router.get("/post/all_user",status_code=status.HTTP_200_OK,response_model=List[new_response_format_for_join])
def get_all_from_post_table(db:Session=Depends(get_db),get_current_user=Depends(auth2.get_current_user),limit:int=2,skip:int=0,search:Optional[str]=""):
    # record=db.query(Post).filter(Post.content.contains(search)).limit(limit).offset(skip).all()
    raw_sql_conversion=db.query(Post,func.Count(Vote.post_id).label("votes")).join(Vote,Post.id==Vote.post_id,isouter=True).group_by(Post.id).filter(Post.content.contains(search)).limit(limit).offset(skip).all()
    print("raw sql:- ",raw_sql_conversion)
    return raw_sql_conversion