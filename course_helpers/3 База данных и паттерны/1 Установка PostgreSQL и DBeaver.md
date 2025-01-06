# Установка PostgreSQL и DBeaver

PostgreSQL — самая популярная СУБД. Она нужна нам, чтобы хранить данные и манипулировать ими.

DBeaver — это одна из самых удобных программ для работы с базой данных:

- легко читать и фильтровать данные в таблицах
- можно строить схемы со связями между таблицами
- можно писать сырой SQL код и запускать его

Так выглядит интерфейс DBeaver:

!["Dbeaver"](/course_helpers/3%20База%20данных%20и%20паттерны/BD1.png)

## Установка PostgreSQL

- Windows: https://selectel.ru/blog/tutorials/ustanovka-postgresql-15-windows/
- Ubuntu: https://firstvds.ru/technology/ustanovka-postgresql-na-ubuntu
- MacOS: https://ploshadka.net/ustanovka-i-podkljuchenie-postgresql-na-mac-os/ или

```shell
brew install postgresql
createuser -s postgres
brew services restart postgresql
```

## Установка DBeaver

- Windows: https://practicum.yandex.ru/blog/menedzher-baz-dannyh-dbeaver/
- Ubuntu: https://losst.pro/ustanovka-dbeaver-v-ubuntu-22-04
- MacOS: https://dbeaver.io/download/ (скачайте и запустите)

## Подключение к базе данных PostgreSQL в DBeaver

!["Dbeaver"](/course_helpers/3%20База%20данных%20и%20паттерны/BD2.png)
!["Dbeaver"](/course_helpers/3%20База%20данных%20и%20паттерны/BD3.png)
!["Dbeaver"](/course_helpers/3%20База%20данных%20и%20паттерны/BD4.png)