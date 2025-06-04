# Работа с Redis

## Настройка Redis

----

### 1 Установка

```bash
sudo apt update
sudo apt install redis-server
```

### 2 Конфигурация Redis

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

## Краткое описание происходящего

Данная инструкция описывает процесс установки, базовой настройки и проверки работы Redis на Linux (Ubuntu/Debian):

1. Обновление списка пакетов и установка Redis с помощью команд sudo apt update и sudo apt install redis-server.

2. Редактирование конфигурационного файла Redis (/etc/redis/redis.conf), где необходимо изменить параметр supervised с
   no на systemd для корректной работы под системой инициализации systemd.

3. Сохранение изменений и перезапуск службы Redis командой sudo systemctl restart redis.service.

4. Проверка работоспособности Redis через команду redis-cli ping, которая должна вернуть ответ PONG.

5. Пример базовых команд Redis через redis-cli: установка ключа (set a 14), получение ключа (get a), удаление ключа (del
   a) и просмотр ключей (keys *).

### Что происходит в целом

Таким образом, инструкция помогает установить Redis, настроить его для работы с systemd и проверить, что сервис
функционирует корректно

---