from fastapi import FastAPI,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware#CORS
from database import Base, engine
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import task2


Base.metadata.create_all(engine)#создание базы данных

app = FastAPI()

origins = [#разрешенные адреса
    "*"
]
app.add_middleware(#разрешения для запросов
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users", response_model = List[schemas.User])#получение всех пользователей
def get_all_users():
    session = Session(bind=engine, expire_on_commit=False)

    all_users = session.query(models.Users).all()

    session.close()

    return all_users
@app.get("/users/{id}", response_model = schemas.User)#получение конкретного пользователя
def read_user_with_id(id:int):
    # создаем соединение с бд
    session = Session(bind=engine, expire_on_commit=False)

    # получаем пользователя с определенным id
    user = session.query(models.Users).get(id)

    # прекращаем соединение
    session.close()

    # если пользователь с таким id существует то передается информация о нем, если его нет то возвращается ошибка
    if not user:
        raise HTTPException(status_code=404, detail=f"пользователь с id = {id} не найден")

    return user
@app.post("/users", response_model = schemas.User, status_code=status.HTTP_201_CREATED)#добавление пользователя
def add_user(user:schemas.User):
    # создаем соединение с базой данных
    session = Session(bind=engine, expire_on_commit=False)

    # собираем данные в соответствии с моделью данных
    usersdb = models.Users(name = user.name, username = user.username, mail = user.mail,
    password = user.password, updated = user.updated, is_active = user.is_active,
    created = user.created, role_id = user.role_id, id = user.id)

    # передаем их через соединение с бд и фиксируем их
    session.add(usersdb)
    session.commit()

    # прекращаем соединение
    session.close()

    return usersdb
@app.put("/users/{id}", response_model = schemas.User)
def put_user(id:int,usera:schemas.User):
    session = Session(bind=engine, expire_on_commit=False)
    # получаем пользователя с определенным id
    user = session.query(models.Users).get(id)
    # обновляем пользователя с полученными данными (если пользователь с данным id есть)
    if user:
        user.name = usera.name
        user.username = usera.username
        user.mail = usera.mail
        user.password = usera.password
        user.updated = usera.updated
        user.is_active = usera.is_active
        user.created = usera.created
        user.role_id = usera.role_id
        user.id = usera.id
        session.commit()

    session.close()

    if not user:
        raise HTTPException(status_code=404, detail=f"пользователь с id = {id} не найден")
    return user
@app.delete("/users/{id}", response_model = schemas.User)
def delete_user(id: int):

    session = Session(bind=engine, expire_on_commit=False)

    user = session.query(models.Users).get(id)

    # если пользователь с данным id есть в базе то удалить его, если нет то вренуть код 404
    if user:
        session.delete(user)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Пользовтаель с id = {id} не найден")

    return user

@app.get("/roles", response_model = List[schemas.Role])
def get_all_roles():
    session = Session(bind=engine, expire_on_commit=False)

    all_roles = session.query(models.Roles).all()

    session.close()

    return all_roles
@app.get("/roles/{id}", response_model = schemas.Role)#получение конкретной роли
def read_role_with_id(id:int):
    session = Session(bind=engine, expire_on_commit=False)

    role = session.query(models.Roles).get(id)

    session.close()

    if not role:
        raise HTTPException(status_code=404, detail=f"роль с id = {id} не найдена")

    return role
@app.post("/roles", response_model = schemas.Role)#добавление роли
def add_role(role:schemas.Role):
    session = Session(bind=engine, expire_on_commit=False)

    rolesdb = models.Roles(name = role.name,  id = role.id)

    session.add(rolesdb)
    session.commit()

    session.close()

    return rolesdb
@app.put("/roles/{id}", response_model = schemas.Role)
def put_role(id:int,rolea:schemas.Role):
    session = Session(bind=engine, expire_on_commit=False)

    role = session.query(models.Roles).get(id)

    if role:
        role.name = rolea.name
        role.id = rolea.id
        session.commit()

    session.close()

    if not role:
        raise HTTPException(status_code=404, detail=f"пользователь с id = {id} не найден")
    return role
@app.delete("/roles/{id}", response_model = schemas.Role)
def delete_role(id: int):

    session = Session(bind=engine, expire_on_commit=False)

    role = session.query(models.Roles).get(id)

    if role:
        session.delete(role)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Роль с id = {id} не найдена")

    return role

#для задания 2
@app.get("/userroles", response_model = List[schemas.Role_Id_Name])
def get_all_userrole():
    session = Session(bind=engine, expire_on_commit=False)

    all_userrole = session.query(models.UserRole).all()

    session.close()
    return all_userrole

@app.post("/userroles/{id}", response_model = schemas.Role_Id_Name)
def add_userrole(id:int):
    session = Session(bind=engine, expire_on_commit=False)
    userrole = task2.roleid_to_roleobj(id)
    userroledb = models.UserRole(name = userrole.name, username = userrole.username, mail = userrole.mail,
    password = userrole.password, updated = userrole.updated, is_active = userrole.is_active,
    created = userrole.created, role = userrole.role, id = userrole.id)

    session.add(userroledb)
    session.commit()

    session.close()

    return userroledb
@app.get("/userroles/{id}", response_model = schemas.Role_Id_Name)
def read_userrole_with_id(id:int):
    
    session = Session(bind=engine, expire_on_commit=False)

    
    userrole = session.query(models.UserRole).get(id)

    
    session.close()

    
    if not userrole:
        raise HTTPException(status_code=404, detail= f"id = {id} не найден")

    return userrole
@app.delete("/userroles/{id}", response_model = schemas.Role_Id_Name)
def delete_user(id: int):

    session = Session(bind=engine, expire_on_commit=False)

    userrole = session.query(models.UserRole).get(id)

    if userrole:
        session.delete(userrole)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"id = {id} не найден")

    return userrole
