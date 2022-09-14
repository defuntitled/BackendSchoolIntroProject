FROM python:3.8-slim-buster

WORKDIR /serv

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV PYTHONPATH /serv
CMD ["python3","service/application.py", "-m" , "flask", "run"]