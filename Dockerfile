FROM python:3.9

WORKDIR /code

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY .env /code/.env

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
