import os
import app.modules.auth.auth_router as auth_router
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI

load_dotenv()

print("JWT SECRET", os.getenv('JWT_SECRET'))

app = FastAPI(title='Simple Auth API')

v1 = APIRouter(prefix='/api/v1') 


@v1.get('/health', tags=['Health Check'])
def health_check():
    yield

v1.include_router(auth_router.router)

app.include_router(v1)

