import os
from uuid import uuid4

from flask import Blueprint, request
from flask.json import jsonify

from elasticsearch import Elasticsearch, exceptions

from src.models import Car, db
from src.utils import car_to_dict

from src.constants.http_status_codes import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT
)

cars = Blueprint("cars", __name__, url_prefix="/api/v1/cars")

es_host = os.environ.get('ELASTICSEARCH_URL', "http://localhost:9200")
print('Elasticsearch host: {}'.format(es_host))
es = Elasticsearch([es_host])

try:
    es.indices.create(index="cars")
except exceptions.BadRequestError:
    pass


def query(state_number, region):
    res = es.search(index='cars', body={
        'query':
            {
                "bool":
                    {
                        "must":
                            [
                                {"match": {"state_number": state_number}},
                                {"match": {"region": region}}
                            ]
                    }
            }
    })
    return res


@cars.post('/')
def create_car():
    state_number = request.get_json().get('state_number', '')
    region = request.get_json().get('region', '')

    if region not in [code[0] for code in Car.REGION_CODE]:
        return jsonify({'error': 'Choice from Region codes'}), HTTP_400_BAD_REQUEST

    res = query(state_number, region)

    if len(res['hits']['hits']) != 0:
        return jsonify({
            'error': 'State Number already taken'
        }), HTTP_409_CONFLICT

    es.index(index='cars', body=request.get_json(), id=uuid4())

    return {"message": "Car created successfully"}, HTTP_201_CREATED


@cars.put('/<id>')
def update_car(id):
    car = es.get(index='cars', id=id)['_source']
    state_number = request.get_json().get('state_number')
    region = request.get_json().get('region')

    if car:
        if not car['state_number'] == state_number and car['region'] == region:

            if region != '' and region not in [code[0] for code in Car.REGION_CODE]:
                return jsonify({'error': 'Choice from Region codes'}), HTTP_400_BAD_REQUEST

            res = query(state_number, region)

            if len(res['hits']['hits']) != 0:
                return jsonify({
                    'error': 'State Number already taken'
                }), HTTP_409_CONFLICT

        es.index(index='cars', id=id, body=request.get_json())

        return {"message": "Car updated successfully"}, HTTP_201_CREATED
    return {"message": "Car not found"}, HTTP_404_NOT_FOUND


@cars.get('/')
def search():
    key = request.args.get('key')
    if key is None:
        res = es.search(index="cars", body={"query": {"match_all": {}}})
    else:
        res = es.search(index="cars", body={"query": {"match": {"state_number": key}}})
    return jsonify(res["hits"]["hits"])


# @cars.post('/')
# def create_car():
#     state_number = request.get_json().get('state_number', '')
#     region = request.get_json().get('region', '')
#     brand = request.get_json().get('brand', '')
#     color = request.get_json().get('color', '')
#
#     if region not in [code[0] for code in Car.REGION_CODE]:
#         return jsonify({'error': 'Choice from Region codes'}), HTTP_400_BAD_REQUEST
#
#     if Car.query.filter_by(region=region, state_number=state_number).first():
#         return jsonify({
#             'error': 'State Number already taken'
#         }), HTTP_409_CONFLICT
#
#     car = Car(state_number=state_number, region=region, brand=brand, color=color)
#     db.session.add(car)
#     db.session.commit()
#
#     return jsonify(car_to_dict(car)), HTTP_201_CREATED


# @cars.get('/')
# def get_cars():
#     page = request.args.get('page', 1, type=int)
#     per_page = request.args.get('per_page', 5, type=int)
#
#     cars = Car.query.paginate(page=page, per_page=per_page)
#
#     data = []
#
#     for car in cars.items:
#         data.append(car_to_dict(car))
#
#     meta = {
#         "page": cars.page,
#         'pages': cars.pages,
#         'total_count': cars.total,
#         'prev_page': cars.prev_num,
#         'next_page': cars.next_num,
#         'has_next': cars.has_next,
#         'has_prev': cars.has_prev,
#
#     }
#
#     return jsonify({'data': data, "meta": meta}), HTTP_200_OK


# @cars.get("/<int:id>")
# def get_car(id):
#     car = Car.query.filter_by(id=id).first()
#
#     if not car:
#         return jsonify({'message': 'Car not found'}), HTTP_404_NOT_FOUND
#
#     return jsonify(car_to_dict(car)), HTTP_200_OK


# @cars.put('/<int:id>')
# @cars.patch('/<int:id>')
# def edit_car(id):
#     car = Car.query.filter_by(id=id).first()
#
#     if not car:
#         return jsonify({'message': 'Car not found'}), HTTP_404_NOT_FOUND
#
#     state_number = request.get_json().get('state_number', car.state_number)
#     region = request.get_json().get('region', car.region)
#     brand = request.get_json().get('brand', car.brand)
#     color = request.get_json().get('color', car.color)
#
#     if Car.query.filter_by(region=region, state_number=state_number).first():
#         return jsonify({
#             'error': 'State Number already taken'
#         }), HTTP_409_CONFLICT
#
#     car.state_number = state_number
#     car.region = region
#     car.brand = brand
#     car.color = color
#
#     db.session.commit()
#
#     return jsonify(car_to_dict(car)), HTTP_200_OK


__all__ = (
    'cars',
)
