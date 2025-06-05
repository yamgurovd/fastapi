# Установка и настройка docker в локальном компьютере для линукса

---

## Docker в локальном компьютере для линукса - https://docs.docker.com/engine/install/ubuntu/

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

----

## Краткое содержание инструкции

В этой инструкции описан процесс установки и базовой настройки Docker на локальном компьютере с Linux (Ubuntu), а также
запуск проекта в контейнере Docker.

### Краткое содержание шагов:

1. Добавляется официальный репозиторий Docker в систему через apt, чтобы получать последние версии пакетов.

2. Устанавливаются необходимые пакеты Docker: сам движок, CLI, containerd и плагины для сборки и docker-compose.

3. Проверяется успешность установки командой запуска тестового контейнера hello-world.

4. Для возможности запускать Docker без sudo пользователь добавляется в группу docker.

`Указывается, что нужно удалить папку /home/d/.docker (вероятно, для сброса локальных настроек) и перезагрузить компьютер.
`

5. Запуск проекта в Docker:

- Переходите в папку с проектом.

- Собираете образ контейнера из Dockerfile командой docker build -t fastapi ..

- Проверяете, что образ создан (docker images).

- Запускаете контейнер с вашим проектом (docker run -it fastapi bash).

- Приведены команды для удаления контейнера и образа при необходимости.

### Что происходит в целом

В целом, инструкция охватывает стандартную установку Docker на Ubuntu и базовые действия для работы с собственными
контейнерам

----