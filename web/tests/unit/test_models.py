from models.cars import Car


def test_create_car():
    car = Car(state_number='123AAA', region='80', brand='BMW', color='red')

    assert car.state_number == '123AAA'
    assert car.region == '80'
    assert car.brand == 'BMW'
    assert car.color == 'red'
