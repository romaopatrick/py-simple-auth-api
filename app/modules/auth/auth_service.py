import datetime
from typing import cast
import uuid
import jwt

from app.boundaries.auth.jwt_schema import JwtPayload
from app.boundaries.auth.login_schema import LoginInput, LoginOutput
from app.boundaries.auth.validate_token_schema import ValidateTokenInput, ValidateTokenOutput
from app.modules.auth.auth_settings import AuthSettings


class AuthService:
    def __init__(self, auth_settings: AuthSettings) -> None:
        self.auth_settings = auth_settings

    
    async 
        
    async def login(self, input: LoginInput) -> LoginOutput:
        generated_at = datetime.datetime.now()

        expires_at = generated_at + datetime.timedelta(
            minutes=self.auth_settings.jwt_expiration_minutes
        )
        
        token = jwt.encode(
            payload=vars(JwtPayload(
                iss= str(uuid.uuid4()),
                iat= int(generated_at.timestamp()),
                sub= str(uuid.uuid4()),
                exp= int(expires_at.timestamp()),
                groups= ["admin"],
                roles= ["admin"],
                permissions= ["admin"],
                name= input.username,
            )),
            key=self.auth_settings.jwt_secret,
        )

        return LoginOutput(
            access_token=token,
            token_type="Bearer",
            expires_at=expires_at,
        )
