from fastapi import FastAPI
from src.fake_users import fake_users

app = FastAPI(
    title="Users app"
)


@app.get("/",
         status_code=200,
         name="Приветствие с пользователем",
         description="name: Имя пользователя")
def hello_person(name: str):
    return f"Привет {name}"


@app.post("/users/{user_id}",
          status_code=201,
          name="Создание нового пользователя",
          description="user_id: Id пользователя \n"
                      "first_name: Имя пользователя \n"
                      "last_name: Фамилия пользователя \n"
                      "patronymic: Отчество пользователя \n"
                      "age: возраст \n"
                      "position: Должность \n"
                      "company: Название компании")
def add_new_user(user_id: int,
                 first_name: str,
                 last_name: str,
                 patronymic: str,
                 age: int,
                 position: str,
                 company: str):

    new_user = {"id": user_id, "first_name": first_name, "last_name": last_name, "patronymic": patronymic,
                "age": age, "position": position, "company": company}

    fake_users.append(new_user)

    return new_user


@app.patch("/users/{user_id}",
           status_code=200,
           name="Изменение данных пользователя",
           description="user_id: id пользователя, \n"
                       "first_name: Имя \n"
                       "last_name: Фамилия \n"
                       "patronymic: Отчество \n"
                       "age: Возраст \n"
                       "position: Должность \n"
                       "company: Название организации")
def update_user_info(user_id: int,
                     first_name: str,
                     last_name: str,
                     patronymic: str,
                     age: int,
                     position: str,
                     company: str):
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


@app.get("/users",
         status_code=200,
         name="Список всех пользователей")
def get_users():
    return fake_users


@app.get("/users/{user_id}",
         status_code=200,
         name="Информация о пользователе",
         description="user_id: id пользователя")
def user_info(user_id: int):
    for user in fake_users:
        # print(user)
        if user["id"] == user_id:
            return user


@app.delete("/users/{user_id}",
            status_code=204,
            name="Удаление записи пользователя",
            description="user_id: id пользователя")
def delete_user_id(user_id: int):
    for user in fake_users:
        if user["id"] == user_id:
            fake_users.remove(user)

        return {"id": user_id}
