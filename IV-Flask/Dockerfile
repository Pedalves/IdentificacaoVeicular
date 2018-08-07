FROM python:3.5.2

RUN apt-get update -y

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8001
CMD ["invoke", "iv"]
