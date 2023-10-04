from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


with open(".env/api_key") as key_file:
    garage_key = key_file.readline().strip()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def authenticate(api_key: str = Depends(oauth2_scheme)):
    if api_key != garage_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)