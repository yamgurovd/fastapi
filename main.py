from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI(
    title="test app"
)

fake_users = [
    {"id": 0, "first_name": "Иванов", "last_name": "Иван", "patronymic": "Иванович", "age": 18,
     "position": "Комплектовщик", "company": "ООО Радуга"},
    {"id": 1, "first_name": "Петров", "last_name": "Андрей", "patronymic": "Иванович", "age": 35,
     "position": "Руководитель", "company": "ООО Радуга"},
    {"id": 2, "first_name": "Андреев", "last_name": "Георгий", "patronymic": "Степанович", "age": 24,
     "position": "Кладовщик", "company": "ООО Радуга"},
    {"id": 3, "first_name": "Макарова", "last_name": "Лидия", "patronymic": "Сергеевна", "age": 20,
     "position": "Оператор", "company": "ООО Радуга"},
    {"id": 4, "first_name": "Андреев", "last_name": "Георгий", "patronymic": "Степанович", "age": 24,
     "position": "Кладовщик", "company": "ООО Радуга"},
    {"id": 5, "first_name": "Сергеева", "last_name": "Ольга", "patronymic": "Петровна", "age": 50,
     "position": "Кассир", "company": "ООО Радуга"},
]


@app.get("/")
def hello_person(name: str):
    """
    :param name: Имя пользователя
    :return: Приветствие с пользователем
    """
    return f"Привет {name}"


@app.post("/users/{user_id}")
def add_new_user(user_id: int,
                 first_name: str,
                 last_name: str,
                 patronymic: str,
                 age: int,
                 position: str,
                 company: str):
    """
    :param user_id: Id пользователя
    :param first_name: Имя пользователя
    :param last_name: Фамилия пользователя
    :param patronymic: Отчество пользователя
    :param age: возраст
    :param position: Должность
    :param company: Название компании
    :return: Создание нового пользователя
    """
    new_user = {"user_id": user_id, "first_name": first_name, "last_name": last_name, "patronymic": patronymic,
                "age": age, "position": position, "company": company}

    fake_users.append(new_user)

    return new_user


@app.patch("/users/{user_id}")
def update_user_info(user_id: int,
                     first_name: str,
                     last_name: str,
                     patronymic: str,
                     age: int,
                     position: str,
                     company: str):
    """
    :param user_id: id пользователя
    :param first_name: Имя пользователя
    :param last_name: Фамилия
    :param patronymic: Отчество
    :param age: Возраст
    :param position: Должность
    :param company: Название организации
    :return:
    """
    user = fake_users[user_id]
    user["first_name"] = first_name
    user["last_name"] = last_name
    user["patronymic"] = patronymic
    user["age"] = age
    user["position"] = position
    user["company"] = company

    fake_users[user_id].update(
        {"id": user_id, "first_name": first_name, "last_name": last_name, "patronymic": patronymic, "age": age,
         "position": position, "company": company})

    return fake_users[user_id]


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """
    :param user_id: id пользователя
    :return: Удаление записи пользователя
    """
    return fake_users.pop(user_id)
@app.get("/users")
def get_users():
    """
    :return: Список всех пользователей
    """
    return fake_users


@app.get("/users/{user_id}")
def get_user_id(user_id: int):
    """
    :param user_id: Ввод id пользователя
    :return: Данные о пользователе
    """
    return fake_users[user_id]
