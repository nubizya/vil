FROM python:3.11.4-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./env.prod /code/env.prod

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "80", "--env-file", "env.prod"]
