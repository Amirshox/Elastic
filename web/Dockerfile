FROM ubuntu:latest
RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python3"]
CMD ["app.py"]