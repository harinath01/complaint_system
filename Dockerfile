FROM python:3.8.20-slim

WORKDIR /workspace/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/prod.txt /workspace/requirements/prod.txt
RUN pip install -r requirements/prod.txt

CMD ["python", "manage.py", "migrate"]
