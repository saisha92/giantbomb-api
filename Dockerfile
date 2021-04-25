ARG BASE_CONTAINER=tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM $BASE_CONTAINER

LABEL author="Saishankar"

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt --use-feature=2020-resolver

COPY ./app /app

ENV PYTHONPATH "${PYTHONPATH}:/app"