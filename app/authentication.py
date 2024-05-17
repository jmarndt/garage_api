import os

from dotenv import load_dotenv
from fastapi import Depends, status, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer


load_dotenv()
API_KEY = os.getenv('API_KEY')


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
def authenticate(req: Request, header_api_key: str = Depends(oauth2_scheme)):
    query_api_key = req.query_params.get('token')
    
    if header_api_key != API_KEY and query_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)