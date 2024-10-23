# fastapi
Ознакомление с FAST api


### 1 Настройка проекта 
1. Создать и активировать виртуальное окружение
```angular2html
python3 -m venv .venv
source .venv/bin/activate
```
2. Установить библиотеку FastAPI
```angular2html
pip install fastapi[all]
```
3. Зафиксировать все библиотеки requirements.txt
```angular2html
python -m pip freeze > requirements.txt
```

### 2 Команды для запуска проекта на локали
1. Запуск проекта на локали 
Remark: флаг --reload необязателен
```angular2html
uvicorn main:app --reload
```

### 3 Дополнительная информация по проекту
1. Доступ к swagger документации - http://127.0.0.1:8000/docs#/