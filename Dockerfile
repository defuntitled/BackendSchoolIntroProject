FROM python:3.8-slim-buster

WORKDIR /serv

COPY . /serv
RUN pip3 install -r requirements.txt
ENV PYTHONPATH /serv
COPY . .
CMD ["python","service/application.py","-m","flask","run"]