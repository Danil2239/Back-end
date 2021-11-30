import schemas
import req


def roleid_to_roleobj(id_of_user):#задание 2
    user = req.get_method(f"http://127.0.0.1:8000/users/{id_of_user}")#получаем данные нужного пользователя
    role = req.get_method(f"http://127.0.0.1:8000/roles/{user['role_id']}")#получаем данные о его роли
    result = schemas.Role_Id_Name(#заносим данные в модель
        name = user["name"],
        username = user["username"],
        mail = user["mail"],
        password = user["password"],
        updated = user["updated"],
        is_active = user["is_active"],
        created = user["created"],
        role = str(role),
        id = user["id"]
    )
    return result# .dict() нужно для того чтобы результат не был str


#t = roleid_to_roleobj(2)


#req.post_method("http://127.0.0.1:8000/userroles",t)
#req.delete_method("http://127.0.0.1:8000/userroles/1")