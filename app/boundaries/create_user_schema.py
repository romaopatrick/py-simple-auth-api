from pydantic import BaseModel

class CreateUserInput(BaseModel):
    username: str
    password: str
    
class CreateUserOutput(BaseModel):
    id: str