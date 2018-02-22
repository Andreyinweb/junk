# python3 sql_models.py

# Импортирует классы таблиц
from models import Role, User, Post_user,session

def print_user():
    """ 
    Печатает данные всей таблицы User(имя 'users')
    """
    # Запрос к таблице User. Выдаст всех пользователей
    sql_request = session.query(User).all()
    # Берет каждого пользователя из запроса
    for use in sql_request :
        # Печатает строку таблицы User
        print(use.id, end=". ")
        print(use.username, end=". ")
        # Печатает значение из таблицы Role
        print(use.roles.name, end=". ")
        print(); print()
        # Берет каждый пост из запроса к таблице Post_user
        for post in use.post :
            # Печатает пост из таблицы Post_user
            print(post.user_post, end="; ")
        print("\n-------------------")




def print_role():
    """
    Печатает данные всей таблицы Role(имя 'roles')
    """
    sql_request = session.query(Role).all()
    for roles in sql_request :
        print(roles.id, end=". ")
        print(roles.name, end=" : ")
        for rol in roles.users :
            print(rol.username, end="; ")
        print()

def print_post():
    """
    Печатает данные всей таблицы Post_user(имя 'posts')
    """
    sql_request = session.query(Post_user).all()
    for post in sql_request :
        print(post.id, end=". ")
        print(post.user_post, end=". ")
        print(post.user.username, end=". ")
        print()

print_user()
print("_____________________________")
print_role()
print("_____________________________")

print_post()

