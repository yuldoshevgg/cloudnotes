FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
RUN ls -la

RUN addgroup --system app && adduser --system --ingroup app app
RUN chown -R app:app /app

USER app

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]