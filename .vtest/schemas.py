from pydantic import BaseModel
#схемы данных pydantic
class User(BaseModel):
    name:str
    username:str
    mail:str
    password:str
    updated:str
    is_active:bool
    created:str
    role_id:int
    id:int
    class Config:
        orm_mode = True
class Role(BaseModel):
    name:str
    id:int
    class Config:
        orm_mode = True
class Role_Id_Name(BaseModel):#задание 2
    name:str
    username:str
    mail:str
    password:str
    updated:str
    is_active:bool
    created:str
    role:str
    id:int
    class Config:
        orm_mode = True