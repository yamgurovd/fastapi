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