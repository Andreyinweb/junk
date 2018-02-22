# python3 run.py

from models import app, db, Role, User, Post_user
from generator import Generator
from random import randint

gener = Generator()

# Удали
db.drop_all() # Удали. Это удаляет все таблицы.
# Удали

# Создает файл базы данных и все таблицы
db.create_all()
print("Создана база данных: " + app.config['SQLALCHEMY_DATABASE_URI'] ) 

# Список ролей для таблицы Role
role_list = ["Admin", "Moderator", "User", "visitor"]

# Список начальных пользователей
users_list = ["God", "Son", "Spirit", "Human"]

# Записывает роли в таблицу Role.(добавляет в сессию базы данных)
for role in role_list:
    role_db = Role (name=role) 
    # Добавляет в сессию базы данных
    db.session.add(role_db)

# Записывает пользователей в таблицу User.
i=1
for use in users_list:
    user_db = User (username=use )
    # Записывает роли связанные по id с таблицей Role. 
    user_db.role_id =  i
    # Добавляет в сессию базы данных
    db.session.add(user_db)    
    i+=1

# Записывает случайных пользователей в таблицу User.
cont = 0
for i in range(1,randint(3,10)):
    user_db = User (username=gener.randomword(5))
    user_db.role_id =  randint(1,4)
    db.session.add(user_db) 
    cont = i   


# Сохраняет  сессию базы данных. 
# Все ранее добавленное в сесию записывается в таблицы.   
try:
    db.session.commit()
    print("Записаны в базу начальные пользователи.")
    print(str(cont) + " случайных пользователей записаны в базу.")   
except :
    print("Или уже создано или ошибка")


# Записывает случайные посты в таблицу Post_user.
cont = 0
# Берет каждого пользователя из запроса
for user_db in User.query.all():
    # Случайное количество постов
    for i in range(0,randint(1,3)):
        # Записывает случайные постыю
        user_post = Post_user(user_post=gener.randomword(randint(10,50)))
        # Записывает пользователей связанные по id с таблицей User.
        user_post.user_id=user_db.id
        # Добавляет в сессию базы данных
        db.session.add(user_post)
        cont +=1
# Сохраняет  сессию базы данных.
try:
    db.session.commit()
    print("Создано " + str(cont) + " ПОСТОВ")   
except :
    print("Или уже создано или ошибка")