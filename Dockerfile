# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.11.2-slim-buster AS builder

WORKDIR /code

COPY requirements.txt /code
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]
CMD ["app.py"]

