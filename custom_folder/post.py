from fastapi import FastAPI,APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from db_connection import engine,get_db
from models import User,Post
import various_format
import main
from custom_folder import auth2

router=APIRouter(
    prefix="/post",
    tags=["Post"]
)

@router.post("/enter_detail",status_code=status.HTTP_201_CREATED,response_model=various_format.response_format)
def enter_detail(details:various_format.enter_detail,db:Session=Depends(get_db),get=Depends(auth2.get_current_user)):
    # converting the pydantic model to dictionary and then send only values
    print("get printable:- ",get)
    new_post=User(**details.dict())
    new_post.password=main.passwd_Context.hash(new_post.password)
    db.add(new_post)
    db.commit()
    # equivalent of returning *
    db.refresh(new_post)
    new_post.password="*"*len(new_post.password)
    return new_post

# inserting values to the post table.
@router.post("/into_post_table",status_code=status.HTTP_200_OK)
def push_data_post_table(details:various_format.post_table_mandatory_fields,db:Session=Depends(get_db),get_cur_usr=Depends(auth2.get_current_user)):
    get_user=db.query(User).filter(User.email==get_cur_usr.email).first()
    get_user_id=get_user.id
    new_post=Post(user_reg_id=get_user_id,**details.dict())
    db.add(new_post)
    db.commit()
    return {"message":"data hasbeen stored successfully"}


# deleting the post from the post table.
@router.delete("/delete_from_post_table/{id}",status_code=status.HTTP_200_OK)
def delete_from_table(id:int,db:Session=Depends(get_db),get_current_user=Depends(auth2.get_current_user)):
    record=db.query(Post).filter(Post.id==id)
    if not record.first():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"there is no record for {id} in the database")
    
    print("get_user_user email:- ",get_current_user.email)
    fetch_user=db.query(User).filter(User.email==get_current_user.email).first()
    fetch_id=fetch_user.id
    if record.first().user_reg_id!=fetch_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Sorry you are not authorized")
    
    record.delete(synchronize_session=False)
    db.commit()

    return {"message":"Data deleted from the database"}


@router.post("/update_from_post_table/{id}",status_code=status.HTTP_200_OK)
def update_from_post_table(id:int,fields:various_format.post_table_update,db:Session=Depends(get_db),get_current_user=Depends(auth2.get_current_user)):
    record=db.query(Post).filter(Post.id==id)
    if not record.first():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"There is no user for {id} in the database")
    record_user=db.query(User).filter(User.email==get_current_user.email).first()
    if record.first().user_reg_id!=record_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not authorized!.")
    
    record.update(fields.dict(),synchronize_session=False)
    db.commit()
    return {'message':"success"}
