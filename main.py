from fastapi import FastAPI
from src.fake_users import fake_users

app = FastAPI(
    title="Users app"
)


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
    new_user = {"id": user_id, "first_name": first_name, "last_name": last_name, "patronymic": patronymic,
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
    :param first_name: Имя
    :param last_name: Фамилия
    :param patronymic: Отчество
    :param age: Возраст
    :param position: Должность
    :param company: Название организации
    :return: Изменение данных пользователя
    """
    for user in fake_users:
        # print(user)
        if user["id"] == user_id:
            user.update({
                "first_name": first_name,
                "last_name": last_name,
                "patronymic": patronymic,
                "age": age,
                "position": position,
                "company": company}, )
            return user


@app.get("/users")
def get_users():
    """
    :return: Список всех пользователей
    """
    return fake_users


@app.get("/users/{user_id}")
def user_info(user_id: int):
    """
    :param user_id: id пользователя
    :return: Информацию о пользователе
    """
    for user in fake_users:
        # print(user)
        if user["id"] == user_id:
            return user


@app.delete("/users/{user_id}")
def delete_user_id(user_id: int):
    """
        :param user_id: id пользователя
        :return: Удаление записи пользователя
        """
    for user in fake_users:
        if user["id"] == user_id:
            fake_users.remove(user)

        return {"id": user_id}
