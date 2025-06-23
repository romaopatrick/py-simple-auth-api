from fastapi import APIRouter, Depends

from app.boundaries.auth.login_schema import LoginInput
from app.modules.auth.auth_service import AuthService
from app.modules.core import container

router = APIRouter(prefix='/auth')

@router.post("/login")
async def login(
    input: LoginInput,
    auth_service: AuthService = Depends(lambda: container.c[AuthService])
    ):
    return await auth_service.login(input)