FROM python:3.7-alpine

ARG APP_ENV=production

ENV APP_ENV=$APP_ENV
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=.

COPY ./requirements /requirements
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install -r /requirements/${APP_ENV}.txt \
    && rm -rf /requirements \
    && apk del .build-deps

WORKDIR /opt
