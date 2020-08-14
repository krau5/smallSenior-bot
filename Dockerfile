FROM python:3.8.3

RUN mkdir -p /usr/src/small-senior-bot
WORKDIR /usr/src/small-senior-bot

COPY . /usr/src/small-senior-bot

RUN pip install -r requirements.txt