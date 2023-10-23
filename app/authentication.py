import os

from dotenv import load_dotenv
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


load_dotenv()
API_KEY = os.getenv('API_KEY')


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def authenticate(api_key: str = Depends(oauth2_scheme)):
    if api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)