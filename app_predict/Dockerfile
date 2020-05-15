FROM python:3.7.3-slim

RUN apt-get update -y

RUN pip install gunicorn

# Setup flask application
COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000

# Start gunicorn
CMD ["gunicorn", "--config", "gunicorn_config.txt", "service.app:app"]

