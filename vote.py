from fastapi import FastAPI,APIRouter,status,Depends,HTTPException
from various_format import vote
from models import Vote
from custom_folder import auth2
from sqlalchemy.orm import Session
from db_connection import get_db
from models import User,Post

router=APIRouter(
    prefix="/vote",
    tags=["Votes"]
)

@router.post("/",status_code=status.HTTP_202_ACCEPTED)
def give_vote(mand_fields:vote,db:Session=Depends(get_db),get_current_user=Depends(auth2.get_current_user)):
    first_check_user_post_table=db.query(Post).filter(Post.id==mand_fields.post_id)
    if not first_check_user_post_table.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Record not found!.")

    user_record=db.query(User).filter(User.email==get_current_user.email).first()
    if not user_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"detail not found!.")
    user_id=user_record.id
    valid_or_not=db.query(Vote).filter(mand_fields.post_id==Vote.post_id,Vote.user_id==user_id) #in db same user found and post fount

    if mand_fields.direction==1:
        if valid_or_not.first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Already there.")
        else:
            new_vote=Vote(user_id=user_id,post_id=mand_fields.post_id)
            db.add(new_vote)
            db.commit()
            return {"message":"in database"}
    
    else:
        if valid_or_not.first():
            valid_or_not.delete(synchronize_session=False)
            db.commit()
            return {"message":'deleted!.'}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"the detail you want to delete that is not present.")
