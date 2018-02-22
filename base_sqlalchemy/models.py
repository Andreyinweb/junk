# python3 models.py

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker

# Показывает точный путь к данному файлу
basedir = os.path.abspath(os.path.dirname(__file__))

# Если echo=True будет печатать все действия
engine = create_engine('sqlite:///' + os.path.join(basedir, 'exempel_data.sqlite'), echo=False)

# 
db = declarative_base() 
Session = sessionmaker(bind=engine)
session = Session()

class Role(db):
    """
    Таблица ролей пользователей
    "Admin", "Moderator", "User", "visitor"
    """
    __tablename__ = 'roles'
    id =  Column( Integer, primary_key=True)
    name =  Column( String(64), unique=True)
    # Связь с таблицей User
    users =  relationship('User', backref='roles', lazy='dynamic')

    def __repr__(self):
        """
        Функция отображения при print()
        Например:
                    [<Role 'Admin'> , <Role 'Son'>]
        """
        return '<Role %r>' % self.name


class User(db):
    """
    Таблица пользователей 
    "God", "Son", "Spirit", "Human"
    """
    __tablename__ = 'users'
    id =  Column( Integer, primary_key=True)
    username =  Column( String(64), unique=True, index=True)
    # Связь с таблицей Role
    role_id =  Column( Integer,  ForeignKey('roles.id'))
    # Связь с таблицей Post_user
    post =  relationship('Post_user', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username


class Post_user(db):
    """
    Таблица постов

    afsyhgihboblHjkKJKJJ7GUJVBNJIVBIJNIK
    """
    __tablename__ = 'posts'
    id =  Column( Integer, primary_key=True)
    user_post =  Column( Text, index=True)
    # Связь с таблицей User
    user_id =  Column( Integer,  ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.user_post
