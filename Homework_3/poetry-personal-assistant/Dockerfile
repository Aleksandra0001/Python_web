FROM python:3.10

ENV POETRY_VERSION=1.1.14
RUN python3 -m pip install poetry==$POETRY_VERSION

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev

COPY . .
SHELL ["powershell", "-command"]
CMD ["poetry", "run", "start"]
