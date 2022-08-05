from src.app import db
from sqlalchemy_utils.types.choice import ChoiceType


class Car(db.Model):
    __tablename__ = 'cars'

    REGION_CODE = [
        (1, 'Tashkent'),
        (30, 'Samarkand'),
        (80, 'Bukhara'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    state_number = db.Column(db.String(6))
    region = db.Column(ChoiceType(REGION_CODE))
    brand = db.Column(db.String(31))
    color = db.Column(db.String(15))

    def __init__(self, state_number, region, brand, color):
        self.state_number = state_number
        self.region = region
        self.brand = brand
        self.color = color

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return '{} {}'.format(self.REGION_CODE, self.state_number)


__all__ = (
    'Car',
)
