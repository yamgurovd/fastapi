FROM python
WORKDIR /work_space/
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt