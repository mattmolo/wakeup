FROM python:2.7

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

ENV WAKEUP_PORT 4000

CMD gunicorn app:app -b 0.0.0.0:$WAKEUP_PORT
