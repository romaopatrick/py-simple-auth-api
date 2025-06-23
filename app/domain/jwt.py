import datetime
from typing import cast
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

from app.boundaries.auth.jwt_schema import JwtPayload
from app.modules.auth.auth_service import AuthService
from app.modules.core import container

def validate_jwt(token: str, secret: str):
    try:
        decoded = jwt.decode(
            jwt=token, 
            key=secret)

        d = cast(JwtPayload, decoded)

        expires_at = datetime.datetime.fromtimestamp(d.exp)
    
        return d
    except jwt.PyJWTError:
        raise ValueError("Invalid authentication credentials")

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        