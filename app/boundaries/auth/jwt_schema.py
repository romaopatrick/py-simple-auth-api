from pydantic import BaseModel


class JwtPayload(BaseModel):
    exp: int
    iat: int
    iss: str
    sub: str
    groups: list[str]
    roles: list[str]
    permissions: list[str]
    name: str