from pydantic_settings import BaseSettings

class AuthSettings(BaseSettings):
    jwt_secret: str = ''
    jwt_expiration_minutes: float = 0
    
    class Config:
        env_file = '.env'
    