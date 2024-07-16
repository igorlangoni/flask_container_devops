FROM python:latest

COPY . /flask_app

RUN pip install flask

CMD python /flask_app/app.py