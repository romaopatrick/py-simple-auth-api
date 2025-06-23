import datetime
from pydantic import BaseModel


class LoginInput(BaseModel):
    username: str
    password: str
    ip: str
    fingerprint: str
    
class LoginOutput(BaseModel):
    access_token: str
    token_type: str
    expires_at: datetime.datetime