# 1) Build: docker build . -t <app name>
#   example: docker build . -t pingpong-app
# 2) Run: docker run -p 8000:8000 pingpong-app
FROM python:3.9-buster
EXPOSE 8000/tcp
WORKDIR /var/app


RUN pip install poetry==1.1.11
COPY pingpong/poetry.lock pingpong/pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install

COPY pingpong/* ./
CMD uvicorn pingpong:app --host=0.0.0.0