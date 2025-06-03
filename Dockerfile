#FROM python:3.12.3
#
#WORKDIR /app
#
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#
#COPY . .
#
#CMD ["python", "src/main.py"]


FROM python:3.12.3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
