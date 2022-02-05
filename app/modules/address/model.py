from .model import get_db

db = get_db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100))
    city = db.Column(db.String(100))
    district = db.Column(db.String(100))
    postal_code = db.Column(db.String(100))
    country = db.Column(db.String(100))


    def __init__(self, street, city, district, postal_code, country):
        self.street = street
        self.city = city
        self.district = district
        self.postal_code = postal_code
        self.country = country


    def update(self, street, city, district, postal_code, country):
        self.street = street
        self.city = city
        self.district = district
        self.postal_code = postal_code
        self.country = country

    def soft_delete(self):
        self._deleted = True
