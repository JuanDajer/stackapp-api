from db.user_db import UserInDB
from db.user_db import update_user, get_user, borrar_user,lista_user,adic_user
from db.movem_db import MovemInDB
from db.movem_db import save_movem

from models.user_models import UserIn, UserOut,GetUser
from models.movem_models import MovemIn,MovemOUT

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()
#########################################################
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "http://localhost:8081","https://stackppapp.herokuapp.com"
    
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
#########################################################

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db != None:
        if user_in_db.password != user_in.password:
            raise HTTPException(status_code=403, detail="El nombre de usuario o contraseña no es válido")
        else:
            return {"auth": True}
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    
    

@api.get("/user/balance/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/movem/")
async def make_movem_add(movem_in: MovemIn):
    user_in_db = get_user(movem_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_in_db.balance = user_in_db.balance + movem_in.value
    update_user(user_in_db)

    movem_in_db = MovemInDB(**movem_in.dict(),actual_saldo = user_in_db.balance)
    movem_in_db = save_movem(movem_in_db)

    movem_out = MovemOUT(**movem_in_db.dict())
    return movem_out

@api.delete("/user/borrar/")
async def user_delete(user_get: GetUser):
    usuario = get_user(user_get.username)
    if usuario == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    else:  
        borrar_user(usuario.username)
        raise HTTPException(status_code=200,
                                detail="El usuario ha sido eliminado")

@api.get("/user/lista/")
async def user_list():
    return lista_user()

@api.post("/createuser/")
async def create_user(user_in: UserInDB):
    user_in_db = get_user(user_in.username)
    if user_in_db != None:
        raise HTTPException (status_code=404, detail="El usuario ya existe")
    else:
        adic_user(user_in)
        return user_in

