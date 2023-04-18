FROM python:3-alpine3.10
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
