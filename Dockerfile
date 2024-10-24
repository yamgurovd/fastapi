## Первая инструкция
#FROM python
#WORKDIR /work_space/
#COPY . .
#RUN python -m pip install --upgrade pip
#RUN pip install -r requirements.txt



## Вторая инструция
#FROM python
#WORKDIR /work_space/
#COPY . .
#RUN python -m pip install --upgrade pip
#RUN pip install -r requirements.txt .
##CMD uvicorn main:app --reload
##CMD python -m pytest -s -v

## Третья инструкция
FROM python
WORKDIR /work_space/
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt .
COPY . .
CMD uvicorn main:app --reload
CMD python -m pytest -s -v