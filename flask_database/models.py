# python3 models.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Показывает точный путь к данному файлу
basedir = os.path.abspath(os.path.dirname(__file__))

# Создает экземпляр класса
app = Flask(__name__)

# Конфигурация Flask
app.config['SECRET_KEY'] = 'hard to guess string'
        # Путь и имя файла базы данных
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'exempel_data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создает экземпляр класса
db = SQLAlchemy(app)


class Role(db.Model):
    """
    Таблица ролей пользователей
    "Admin", "Moderator", "User", "visitor"
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # Связь с таблицей User
    users = db.relationship('User', backref='roles', lazy='dynamic')

    def __repr__(self):
        """
        Функция отображения при print()
        Например:
                    [<Role 'Admin'> , <Role 'Son'>]
        """
        return '<Role %r>' % self.name


class User(db.Model):
    """
    Таблица пользователей 
    "God", "Son", "Spirit", "Human"
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # Связь с таблицей Role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # Связь с таблицей Post_user
    post = db.relationship('Post_user', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username


class Post_user(db.Model):
    """
    Таблица постов

    afsyhgihboblHjkKJKJJ7GUJVBNJIVBIJNIK
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_post = db.Column(db.Text, index=True)
    # Связь с таблицей User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.user_post
