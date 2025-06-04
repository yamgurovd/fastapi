# Установка и настройка БД - PostgreSQL

---

## Установка PostgreSQL

### 1 Установка и настройка

```bash
sudo apt update
sudo apt install postgresql
sudo systemctl start postgresql.service
```

### 2 Работа с PostgreSQL

```bash
sudo -i -u postgres
psql
```

### 3 Создание базы данных

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

### Пример

![Работа с PostgreSQL](/course_helpers/3%20База%20данных%20и%20паттерны/BD5.png)

---

## Краткое описание происходящего

В инструкции описывается процесс установки и базовой настройки базы данных PostgreSQL на системе Linux (Ubuntu):

1. Сначала обновляется список пакетов командой sudo apt update.

2. Затем устанавливается PostgreSQL с помощью sudo apt install postgresql.

3. После установки запускается служба PostgreSQL командой sudo systemctl start postgresql.service.

4. Для работы с базой данных переключаются на пользователя postgres (sudo -i -u postgres) и запускается консоль psql.

5. В консоли создаётся новая база данных командой SQL CREATE DATABASE hotel_db;.

`Приводятся полезные команды для работы с PostgreSQL: просмотр списка баз (\l), подключение к базе (\c dbname), просмотр
таблиц (\dt).`

### Что происходит в целом

Таким образом, инструкция показывает, как установить PostgreSQL, запустить сервис, войти в консоль и создать базу данных
для дальнейшей работы


---