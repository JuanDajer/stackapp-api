from pydantic import BaseModel
from datetime import datetime

class MovemIn(BaseModel):
    username: str
    value: int
class MovemOUT(BaseModel):
    id_movem: int
    username: str
    fecha: datetime
    value: int
    actual_saldo: int