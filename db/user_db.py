from typing import Dict
from pydantic import BaseModel

#Definición de UserInDB
class UserInDB(BaseModel):
    nombre: str
    apellido: str
    username: str
    email:str
    year: int
    password: str
    balance: int

# Base de datos ficticia 
database_users = Dict[str, UserInDB]
database_users = {
    "jsdajerp": UserInDB(**{"nombre":"Juan",
                            "apellido":"Dajer",
                            "username":"jsdajerp",
                            "email":"dajerjuansaid@gmail.com",
                            "year":1993,
                            "password":"root",
                            "balance":1000000}),
    "afgarciap": UserInDB(**{"nombre":"Andrés",
                            "apellido":"García",
                            "username":"afgarciap",
                            "email":"andres.perea@hotmail.com",
                            "year":1994,
                            "password":"root1",
                            "balance":1100000}),
    "srinconz": UserInDB(**{"nombre":"Santiago",
                            "apellido":"Rincón",
                            "username":"srinconz",
                            "email":"chago591@hotmail.com",
                            "year":1992,
                            "password":"root2",
                            "balance":1200000}),
    "dacaidedom": UserInDB(**{"nombre":"David",
                            "apellido":"Caicedo",
                            "username":"dacaicedom",
                            "email":"david.merchancano@correounivalle.edu.co",
                            "year":1993,
                            "password":"root3",
                            "balance":1300000}),
}
#Funciones sobre la base de datos ficticia
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

def borrar_user(username: str):
    if username in database_users.keys():
        database_users.pop(username)
    else:
        return None
def lista_user():
    lista=[]
    for i in database_users:
        a = "Nombre:",database_users[i].nombre,"Apellido:",database_users[i].apellido,"UserName:",database_users[i].username,"Saldo",database_users[i].balance
        lista.append(a)
    return lista

def adic_user(user_in_db: UserInDB):
    if user_in_db.username in database_users.keys():
        return "fail"
    else:
        a = {user_in_db.username: user_in_db}
        database_users.update(a)
        return "Registro exitoso"
#implementar control de saldo