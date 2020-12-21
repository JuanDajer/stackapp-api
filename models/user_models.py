from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
class UserOut(BaseModel):
    nombre: str
    apellido: str
    username: str
    balance: int
class GetUser(BaseModel):
    username: str