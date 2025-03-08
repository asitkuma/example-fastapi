from jose import JWTError
from datetime import datetime,timedelta,UTC,timezone
import various_format
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
import jwt
from config import setting

SECRET_KEY=setting.secret_key
ALGORITHM=setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=setting.access_token_expire_minutes

# creation of object of class OAuth2PasswordBearer
# from login we are getting the access token.
oAuth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    
def verify_access_token(token:str,credential_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        email:str=payload.get("email")
        password:str=payload.get("password")
        
        if not email or not password:
            raise credential_exception
        # this is the creation of the object of class named Token.
        token_data=various_format.Token(email=email,password=password)
        print("Token Data:- ",token_data)
    except JWTError:
        print("some error occured")
        raise credential_exception

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Session expired login again")
    
    return token_data
    
def get_current_user(token:str=Depends(oAuth2_scheme)):
    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Not valid credential",headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,credential_exception)