from pydantic import BaseModel

from app.boundaries.auth.jwt_schema import JwtPayload


class ValidateTokenInput(BaseModel):
    token: str

class ValidateTokenOutput(BaseModel):
    valid: bool
    data: JwtPayload
    