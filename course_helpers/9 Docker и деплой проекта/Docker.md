# Работа с Docker 

## Установка и настройка docker в локальном компьютере для линукса - https://docs.docker.com/engine/install/ubuntu/

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

## Инструкция для запуска Docker с БД, Redis и Backend

### Создание сети Docker для взаимодействия Postgres, Redis и Backend

```shell
docker network create myNetwork
```

![Dbeaver](/course_helpers/9%20Docker%20и%20деплой%20проекта/dcoker_network.png)

### Запуск Postgres в Docker-контейнере

```shell
docker run --name booking_db_1 \
    -p 6432:5432 \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=booking \
    --network myNetwork \
    --volume pg-booking-data:/var/lib/postgresql/data \
    -d postgres:16
```

#### Настройки подключения к базе данных (пример .env)

```text
MODE=LOCAL

DB_HOST=booking_db_1
DB_PORT=6432       # Здесь изменить при необходимости
DB_USER=postgres   # Здесь изменить при необходимости
DB_PASS=password   # Здесь изменить при необходимости
DB_NAME=booking

REDIS_HOST=booking_redis
REDIS_PORT=7379

JWT_SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

![Dbeaver](/course_helpers/9%20Docker%20и%20деплой%20проекта/docker_DB1.png)

### Запуск Redis в Docker-контейнере

```shell
docker run --name booking_redis \
    -p 7379:6379 \
    --network=myNetwork \
    -d redis:7.4
```

#### Настройка Redis в локальном .env файле

```text
MODE=LOCAL

DB_HOST=booking_db
DB_PORT=6432
DB_USER=postgres
DB_PASS=password 
DB_NAME=booking

REDIS_HOST=booking_redis # Здесь изменить при необходимости 
REDIS_PORT=7379          # Здесь изменить при необходимости

JWT_SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
![Dbeaver](/course_helpers/9%20Docker%20и%20деплой%20проекта/docker_redis.png)
### Запуск Backend в Docker-контейнере

```shell
docker run --name booking_back \
    -p 7777:8000 \
    --network=myNetwork \
    booking_image
```

### Запуск Celery в Docker-контейнере

```shell
docker run --name booking_celery_worker \
    --network=myNetwork \
    booking_image \
    celery --app=src.tasks.celery_app:celery_instance worker -l INFO
```

### Запуск Celery-beat в Docker-контейнере

```shell
docker run --name booking_celery_beat \
    --network=myNetwork \
    booking_image \
    celery --app=src.tasks.celery_app:celery_instance worker -l INFO -B
```

### Сборка образа Backend части приложения

```shell
docker build -t booking_image .
```
![Dbeaver](/course_helpers/9%20Docker%20и%20деплой%20проекта/docker_back.png)

----

## Краткое содержание инструкции

инструкция описывает процесс запуска и настройки нескольких сервисов (Postgres, Redis, Backend, Celery) в
Docker-контейнерах с использованием пользовательской Docker-сети для их взаимодействия.

### Краткий обзор происходящего

1. Создание Docker-сети
   Команда docker network create myNetwork создаёт отдельную мостовую сеть Docker, позволяющую контейнерам общаться друг
   с другом по именам и IP внутри этой сети.

2. Запуск Postgres
   Запускается контейнер с базой данных Postgres, с пробросом порта 6432 на хост и подключением к созданной сети
   myNetwork. Данные сохраняются в Docker volume pg-booking-data для постоянства данных. Параметры пользователя, пароля
   и имени базы задаются через переменные окружения.

3. Настройка подключения к Postgres
   Пример файла .env содержит параметры подключения к базе данных и Redis, а также настройки JWT для аутентификации в
   backend.

4. Запуск Redis
   Контейнер Redis запускается с пробросом порта 7379 и подключением к той же сети myNetwork. Порт Redis внутри
   контейнера — 6379, но на хосте проброшен как 7379 (возможно, чтобы избежать конфликта).

5. Запуск Backend
   Запускается контейнер с backend-приложением, проброшен порт 7777 на 8000 внутри контейнера, подключён к сети
   myNetwork.

6. Запуск Celery и Celery-beat
   Запускаются контейнеры для фоновых задач (worker) и планировщика задач (beat) Celery, используя тот же образ backend
   и сеть myNetwork.

7. Сборка образа backend
   Команда docker build -t booking_image . создаёт образ backend-приложения из текущей директории.

### Что происходит в целом

В итоге, инструкция описывает создание изолированной сети Docker и запуск в ней базы данных Postgres, кеша Redis,
backend-приложения и фоновых задач Celery, обеспечивая их взаимодействие и сохранность данных.

----