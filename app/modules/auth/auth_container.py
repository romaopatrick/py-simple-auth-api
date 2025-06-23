from lagom import Container

from app.modules.auth.auth_service import AuthService
from app.modules.auth.auth_settings import AuthSettings


def auth_container(c: Container) -> Container:
    c[AuthSettings] = AuthSettings()
    c[AuthService] = AuthService
    
    return c