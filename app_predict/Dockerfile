FROM python:3.7.1

RUN apt-get update -y

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["webapp/app.py"]