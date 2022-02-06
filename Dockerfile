FROM python:3.8.10-slim

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt


RUN pip install -e /src/app

ENV FLASK_ENV development
ENV FLASK_APP api/main

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "9999"]
