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

## 5. Линтер и форматтер Ruff

### запуск проверки линтеров

```shell
ruff check
```

### Форматирование кода - отформатирует все директироии

```shell
ruff format
```

### Форматирование конкретной директории

```shell
ruff format src
```

## Статический типизатор Pyright

### Установка на linux

```shell
sudo npn install -g pyright
```

### Проверка работы на типизацию

```shell
pyright
```

### Пример использования

!["Dbeaver"](/course_helpers/7%20Тестирование/pyright.png)


---

## 3 Установка и настройка docker в локальном компьютере для линукса - https://docs.docker.com/engine/install/ubuntu/

1. Set up Docker's apt repository.

```shell
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

2. Install the Docker packages.

```shell
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the Docker Engine installation is successful by running the hello-world image.

```shell
sudo docker run hello-world
```

4. Для запуска docker без sudo необходимо сделать:

```shell
sudo usermod -aG docker $USER
```

5. /home/d/.docker - В директории на локальном компьютере удалить папку
6. Выполнить reboot

## 3.1 Запуск проекта в Docker

1. Перейти в директорию проекта на локальном компьютере через терминал пример:
   <img alt="Пример" height="100" src="![img.png](img.png)" title="Пример" width="100"/>
2. Собрать образ контейнера

```shell
docker build -t fastapi .
```

3. Проверить добавление образа

```shell
docker images
```

4. Запустить проект внутри контейнера

```shell
docker run -it fastapi bash
```

5. Команды, чтобы удалить контейнер и образ

```shell
docker rm <id_container>
docker rmi <id_images>
```

## Запуск Redis в Docker

### Просмотр образов на локальном компьютере

```shell
docker images
```

### Скачать образ Redis из dockerhub

```shell
docker pull redis:7.4
```

### Прокинуть порт 1234

```shell
docker run -p 1234:6379 redis
```

!["Dbeaver"](/course_helpers/9%20Docker%20и%20деплой%20проекта/redis_docker_1.png)

### Запуск redis-cli в docker

```shell
docker run -p 1234:6379 redis
```

!["Dbeaver"](/course_helpers/9%20Docker%20и%20деплой%20проекта/redic_docker.png)

### Посмотреть образы

```shell
docker ps
```

### Определить на каком порту крутиться redis

!["Dbeaver"](/course_helpers/9%20Docker%20и%20деплой%20проекта/redis_docker_3.png)

### Переходим в локалхост

```angular2html
http://localhost:18123
```

!["Dbeaver"](/course_helpers/9%20Docker%20и%20деплой%20проекта/redis_docker_2.png)

## Запуск проекта с Dockerfile

### 1. Сборка образа

```shell
docker build -t booking_image_1 .
```

### 2. Просмотр списка образов

```shell
docker images
```

### 3. Запуск контейнера из образа

```shell
docker run booking_image_1
```

### Пример

![Dbeaver](/course_helpers/9%20Docker%20и%20деплой%20проекта/docker_1.png)

### 4. Запуск контейнера с пробросом портов

```shell
docker run -p 8888:8000 booking_image_1
```

![Dbeaver](/course_helpers/9%20Docker%20и%20деплой%20проекта/docker_2.png)


----

## Запуск Swagger-документации на двух машинах

### Проверка IP-адресов на обоих компьютерах

На каждом из компьютеров выполните команду:

```shell
ip a
```

### Пример вывода на компьютере с сервером

```shell
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: enp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether d8:43:ae:52:20:58 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.102/24 brd 192.168.0.255 scope global dynamic noprefixroute enp3s0
       valid_lft 4064sec preferred_lft 4064sec
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 56:fb:3c:26:2a:38 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::54fb:3cff:fe26:2a38/64 scope link 
       valid_lft forever preferred_lft forever
```

### Пример вывода на ноутбуке

```shell
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute 
       valid_lft forever preferred_lft forever
2: enp14s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether e8:40:f2:9f:a9:29 brd ff:ff:ff:ff:ff:ff
3: wlp13s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 44:6d:57:1c:e0:30 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.100/24 brd 192.168.0.255 scope global dynamic noprefixroute wlp13s0
       valid_lft 6927sec preferred_lft 6927sec
    inet6 fe80::fe60:c9e3:5e74:b492/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

### Проверка сетевого соединения

#### IP компьютера с сервером: 192.168.0.102/24

#### IP ноутбука: 192.168.0.100/24

#### Оба устройства находятся в одной подсети 192.168.0.0/24, значит они должны видеть друг друга.

#### Проверьте с ноутбука доступность компьютера с сервером командой:

```shell
ping 192.168.0.102
```

#### Пример успешного ответа:

```shell
PING 192.168.0.102 (192.168.0.102) 56(84) bytes of data.
64 bytes from 192.168.0.102: icmp_seq=1 ttl=64 time=4.21 ms
64 bytes from 192.168.0.102: icmp_seq=2 ttl=64 time=1.56 ms
64 bytes from 192.168.0.102: icmp_seq=3 ttl=64 time=13.5 ms
```

...

### Открытие Swagger-документации в браузере

#### На ноутбуке откройте в браузере следующий адрес:

```text
http://192.168.0.102:8000/docs#
```