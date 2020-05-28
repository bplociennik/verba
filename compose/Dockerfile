ARG PYTHON_VERSION=3.8.3-slim-buster

FROM python:${PYTHON_VERSION} as build
WORKDIR /wheels
COPY ./requirements.txt /wheels/

RUN apt-get update && apt-get install -y --no-install-recommends
RUN pip install -U pip && pip wheel -r requirements.txt


FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED 1
COPY --from=build /wheels /wheels

RUN pip install --no-cache-dir -r /wheels/requirements.txt -f /wheels && \
    rm -rf /wheels && rm -rf /root/.cache/pip/*
WORKDIR /code
COPY . /code

ENTRYPOINT ["/code/compose/entrypoint.sh"]
