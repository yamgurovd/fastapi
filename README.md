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
