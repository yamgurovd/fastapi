# FastAPI: Система бронирования отелей

## Краткое описание
```markdown


Проект для бронирования отелей с использованием библиотеки FastAPI. Разработан в рамках обучающего курса:  
[https://artemshumeiko.zenclass.ru/public/products](https://artemshumeiko.zenclass.ru/public/products)

![Логотип FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

```

---

## 1. Настройка проекта

### 1.1 Создание виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 1.2 Установка FastAPI

```bash
pip install fastapi[all]
```

### 1.3 Сохранение зависимостей

```bash
python -m pip freeze > requirements.txt
```

---

## 2. Запуск проекта

Доступные способы запуска на локальной машине:

#### Способ 1 (с авто-перезагрузкой)

```bash
uvicorn main:app --reload
```

#### Способ 2

```bash
fastapi dev main.py
```

#### Способ 3

```bash
python main.py
```

*Примечание:* Для продакшн-окружения рекомендуется использовать первый способ без `--reload`

![Пример запуска сервера](course_helpers/3%20База%20данных%20и%20паттерны/BD5.png)

---

## 3. Установка PostgreSQL

### 3.1 Установка и настройка

```bash
sudo apt update
sudo apt install postgresql
sudo systemctl start postgresql.service
```

### 3.2 Работа с PostgreSQL

```bash
sudo -i -u postgres
psql
```

### 3.3 Создание базы данных

```sql
CREATE
DATABASE hotel_db;
```

### Полезные команды:

| Команда     | Описание         |
|-------------|------------------|
| `\l`        | Список БД        |
| `\c dbname` | Подключение к БД |
| `\dt`       | Список таблиц    |

![Работа с PostgreSQL](course_helpers/3%20База%20данных%20и%20паттерны/BD5.png)

---

## 4. Настройка Redis

### 4.1 Установка

```bash
sudo apt update
sudo apt install redis-server
```

### 4.2 Конфигурация Redis

1. Откройте конфигурационный файл:

```bash
sudo nano /etc/redis/redis.conf
```

2. Найдите секцию GENERAL (Ctrl+W для поиска):

Исходный вид секции:

```ini
################################# GENERAL #####################################

# By default Redis does not run as a daemon. Use 'yes' if you need it.
daemonize yes

# If you run Redis from upstart or systemd, Redis can interact with your
# supervision tree. Options:
#   supervised no
#   supervised systemd
#   supervised auto
# supervised auto

pidfile /var/run/redis/redis-server.pid
```

3. Добавьте строку `supervised systemd` после комментариев:

```ini
################################# GENERAL #####################################

# By default Redis does not run as a daemon. Use 'yes' if you need it.
# Note that Redis will write a pid file in /var/run/redis.pid when daemonized.
# When Redis is supervised by upstart or systemd, this parameter has no impact.
daemonize yes

# If you run Redis from upstart or systemd, Redis can interact with your
# supervision tree. Options:
#   supervised no      - no supervision interaction
#   supervised upstart - signal upstart by putting Redis into SIGSTOP mode
#                        requires "expect stop" in your upstart job config
#   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET
#                        on startup, and updating Redis status on a regular
#                        basis.
#   supervised auto    - detect upstart or systemd method based on
#                        UPSTART_JOB or NOTIFY_SOCKET environment variables
# Note: these supervision methods only signal "process is ready."
#       They do not enable continuous pings back to your supervisor.
#
# The default is "no". To run under upstart/systemd, you can simply uncomment
# the line below:
#
# supervised auto
supervised systemd ---- ВОТ ЗДЕСЬ НУЖНО ДОБАВИТЬ 
```

4. Сохранение изменений:

- Нажмите `Ctrl+O` для сохранения
- Нажмите `Enter` для подтверждения
- Нажмите `Ctrl+X` для выхода

5. Перезапустите Redis:

```bash
sudo systemctl restart redis.service
```

### 4.3 Проверка работы

```bash
redis-cli ping
```

Ожидаемый ответ: `PONG`

### Пример работы черз redis-cli

```redis
d@d:~$ redis-cli
127.0.0.1:6379> set a 14
OK
127.0.0.1:6379> keys *
1) "a"
127.0.0.1:6379> values *
(error) ERR unknown command 'values', with args beginning with: '*'
127.0.0.1:6379> value a
(error) ERR unknown command 'value', with args beginning with: 'a'
127.0.0.1:6379> get a
"14"
127.0.0.1:6379> del a
(integer) 1
127.0.0.1:6379> keys *
(empty array)
```

---

## 5. Миграции с Alembic

### 5.1 Установка

```bash
pip install sqlalchemy alembic
```

### 5.2 Инициализация

```bash
alembic init migrations
```

### 5.3 Создание и применение миграции

```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

![Пример миграций](course_helpers/3%20База%20данных%20и%20паттерны/alembic_migrations_example1.png)

---

## 6. Интеграция Celery

### 6.1 Запуск воркера

```bash
celery --app=src.tasks.celery_app:celery_instance worker -l info
```

### 6.2 Запуск с Beat

```bash
celery --app=src.tasks.celery_app:celery_instance worker -l info -B
```

### Пример задач:

```python
@app.task
def send_confirmation_email(booking_id):
# Логика отправки email
```

---

## 7. Тестирование

### Запуск тестов

```bash
pytest -v
```

### Покрытие кода

```bash
pytest --cov=app tests/
```

![Пример тестирования](course_helpers/tests/test_example.png)

---

## Контакты

По вопросам сотрудничества:  
[example@email.com](mailto:example@email.com)

![Финал архитектуры](course_helpers/architecture_final.png)