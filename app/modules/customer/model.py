from .model import get_db

db = get_db()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    id_address = db.Column(db.Integer, db.ForeignKey('address.id'))
    id_bank_account = db.Column(db.Integer, db.ForeignKey('bank_account.id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())
    status = db.Column(db.Boolean)
    _deleted = db.Column(db.Boolean)


    def __init__(self, name, cpf, id_address=None, id_bank_account=None, created_at = datetime.utcnow(), status=True, _deleted=False):
        self.name = name
        self.cpf = cpf
        self.id_address = id_address
        self.id_bank_account = id_bank_account
        self.status = status
        self._deleted = _deleted

    def update(self, name, cpf, id_address=None, id_bank_account=None, status=True, _deleted=False):
        self.name = name
        self.cpf = cpf
        self.id_address = id_address
        self.id_bank_account = id_bank_account
        self.status = status
        self._deleted = _deleted

    def soft_delete(self):
        self._deleted = True

