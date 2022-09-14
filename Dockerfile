FROM python:3.8-slim-buster



COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
WORKDIR /service
ENV PYTHONPATH /
CMD ["gunicorn","--workers=10","--bind","0.0.0.0:80", "application:app"]