from fastapi import Depends,status,APIRouter,HTTPException
from various_format import enter_detail
from db_connection import get_db
from sqlalchemy.orm import Session
from models import User
import main
from fastapi.encoders import jsonable_encoder
# from auth2 import create_access_token
from custom_folder import auth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import various_format

router=APIRouter(
    prefix="/user",
    tags=["Authentication"]
)

@router.post("/login",status_code=status.HTTP_200_OK,response_model=various_format.Output_Token)
def valid_user(mandatory_detail:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    record=db.query(User).filter(User.email==mandatory_detail.username).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There is no user found for this email={mandatory_detail.email}")
    if not main.passwd_Context.verify(mandatory_detail.password,record.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Password error.")
    
    access_token=auth2.create_access_token(data=jsonable_encoder(record))

    return {"token":access_token,"token_type":"Bearer"}