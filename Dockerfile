FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/

RUN apk upgrade --update && \
    apk add build-base libxml2-dev libxslt-dev jpeg-dev zlib-dev

ENV MAKEFLAGS="-j10"
RUN pip install -r ./requirements.txt

ADD ./ /code/
