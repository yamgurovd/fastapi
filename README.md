# fastapi

## Краткое описание

Проект бронирование отелей c библиотекой fastapi изучение курса - https://artemshumeiko.zenclass.ru/public/products

## 1 Настройка проекта

1. Создать и активировать виртуальное окружение

```angular2html
python3 -m venv .venv
source .venv/bin/activate
```

2. Установить библиотеку fastapi

```angular2html
pip install fastapi[all]
```

3. Зафиксировать все библиотеки requirements.txt

```angular2html
python -m pip freeze > requirements.txt
```

## 2 Команды для запуска проекта на локальном компьютере

1. Запуск проекта на локальном компьютере тремя способами

#### 1 способ, флаг --reload не обязательный

```angular2html
uvicorn main:app --reload
```

#### 2 способ

```angular2html
fastapi dev main.py
```

#### 3 способ если на

```angular2html
python main.py
```

#### Remark: Данный вид запуска применяется при разворачивании проекта на сервере

## 3 Установка PostgreSQL

Инструкция взята -  https://firstvds.ru/technology/ustanovka-postgresql-na-ubuntu

### в консоли:

- 1

```shell
sudo apt update
```

- 2

```shell
sudo apt install postgresql
```

- 3

```shell
sudo systemctl start postgresql.service
```

#### Remark  если установлен постгрес начать с этого шага

- 4

```shell
sudo -i -u postgres
```

- 5

```sql
psql
```

- 6

```sql
create database testdb;
```

#### Remark  не забудь кавычки

### Полезные команды для SQL

- в psql команды надо заканчивать символом ;
- \l вводишь в psql, это список бд
- при успешном создании бд будет ответ CREATE DATABASE
- q - для выхода после команды

### Пример установки PostgreSQL

!["PostgreSQL"](/course_helpers/3%20База%20данных%20и%20паттерны/BD5.png)

## Взаимодействие БД с помощью sqlalchemy и alembic

### Установка

1. Установка библиотек для запросов к БД

```shell
pip install sqlalchemy alembic
```

2Установка библиотек для запросов к БД

```shell
pip install sqlalchemy alembic
```

### Миграции

1. Инициализация и настройка директорий для миграций

```shell
alembic init src/migrations
```

2. Подготовка миграции для создания таблиц и выполнение обновлений

```shell
alembic revision --autogenerate -m "initial_migration"
```

3. Создание таблицы в БД

```shell
alembic upgrade head
```

### Пример выполнения миграции

!["PostgreSQL"](/course_helpers/3%20База%20данных%20и%20паттерны/alembic_migrations_example1.png)

## Установка Redis

1. Обновите пакеты:

```shell
sudo apt update
sudo apt upgrade
```
2. Установите Redis:
```shell
sudo apt install redis-server
```
3. Откройте конфигурационный файл:
```shell
sudo nano /etc/redis/redis.conf
```
4. Найдите секцию GENERAL (используйте поиск Ctrl+W и введите GENERAL) - Она выглядит примерно так:
```text
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
5. Добавьте строку supervised systemd после комментариев, но перед другими параметрами (например, pidfile):
```text
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
6. После этого сохраните изменения с помощью комбинации клавиш Ctrl + O. Затем закройте файл сочетанием Ctrl + X.
7. Перезапустите службу Redis:
```shell
sudo systemctl restart redis.service
```
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


## Celery
Для запуска Celery необходимо запустить команду
```shell
celery --app=src.tasks.celery_app:celery_instance worker -l info
```

Полезные команды:
Запуск воркера с указанием конкретных очередей:
```shell
celery -A proj worker -l INFO -Q foo,bar,baz
```
### Управление воркерами и очередями
Добавить потребителя (воркера) для очереди:
```shell
celery -A proj control add_consumer foo
```

### Вызов задач из Python-кода
Вызов задачи асинхронно с помощью delay():
```shell
result = add.delay(4, 4)
```
Параллельное выполнение группы задач (group):
```shell
from celery import group
group_result = group(add.s(2, 2), add.s(4, 4))()
```
Просмотр справки по команде worker
```shell
celery worker --help
```