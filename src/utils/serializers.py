from src.models import Car


def car_to_dict(car: Car):
    car_dict = {
        'id': car.id,
        'url': car.state_number,
        'region': {'name': car.region.value, 'code': car.region.code},
        'visit': car.brand,
        'body': car.color,
    }
    return car_dict
