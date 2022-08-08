# ELASTIC

![python](https://img.shields.io/badge/-python-grey?style=for-the-badge&logo=python&logoColor=white&labelColor=306998)
![flask](https://img.shields.io/badge/-flask-grey?style=for-the-badge&logo=flask&logoColor=white&labelColor=green)
![elasticsearch](https://img.shields.io/badge/-elasticsearch-grey?style=for-the-badge&logo=elasticsearch&logoColor=white&labelColor=red)

## <b>Installation</b> (For Linux)

```bash 
git clone https://github.com/Amirshox/Elastic.git
````

```bash 
cd Elastic
```

```bash
pip install -r requirements.txt
```

### And you have to install Elasticsearch

[https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)

### Run Flask server

```bash
python app.py
```

# API ENDPOINTS

## GET

[localhost:5000/api/v1/cars?key=<state_number>](localhost:5000/api/v1/cars?key=<state_number>)

## POST

[localhost:5000/api/v1/cars](localhost:5000/api/v1/cars)

### body = {

#### "state_number": "12345",

#### "region": "01"

#### "brand": "Corolla",

#### "color": "red",

### }

## PUT

[localhost:5000/api/v1/cars/<eid</](localhost:5000/api/v1/cars/<id>)

### body = {

#### "state_number": "12345",

#### "region": "01"

#### "brand": "Corolla",

#### "color": "red",

### }