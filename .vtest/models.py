from sqlalchemy import Column, Integer, String, BOOLEAN
from database import Base
#таблицы в бд
# Создаем класс который наследуется от базового
class Users(Base):
    __tablename__ = "users" #название таблицы
    #столбцы
    name = Column(String(256))
    username = Column(String(256))
    mail = Column(String(256))
    password = Column(String(256))
    updated = Column(String(256))
    is_active = Column(BOOLEAN)
    created = Column(String(256))
    role_id = Column(Integer)
    id = Column(Integer, primary_key = True)
class Roles(Base):
    __tablename__ = "roles"
    name = Column(String(256))
    id = Column(Integer, primary_key = True)
class UserRole(Base):
    __tablename__ = "userrole"
    name = Column(String(256))
    username = Column(String(256))
    mail = Column(String(256))
    password = Column(String(256))
    updated = Column(String(256))
    is_active = Column(BOOLEAN)
    created = Column(String(256))
    role = Column(String(256))
    id = Column(Integer, primary_key = True)