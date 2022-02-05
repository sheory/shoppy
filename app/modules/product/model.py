from .model import get_db

db = get_db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Numeric)
    quantity = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    _deleted = db.Column(db.Boolean)


    def __init__(self, name, price, quantity, status=True, _deleted=False):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self._deleted = _deleted


    def update(self, name, price, quantity, status=True, _deleted=False):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status
        self._deleted = _deleted

    def soft_delete(self):
        self._deleted = True
