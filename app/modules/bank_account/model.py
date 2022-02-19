from .model import get_db

db = get_db()

class BankAccount(db.Model):
    __tablename__ = 'bank_account'

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer)
    agency = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    _deleted = db.Column(db.Boolean)


    def __init__(self, account, agency, status=True, _deleted = False):
        self.account = account
        self.agency = agency
        self.status = status
        self._deleted = _deleted


    def update(self, account, agency, status=True, _deleted = False):
        self.account = account
        self.agency = agency
        self.status = status
        self._deleted = _deleted

    def soft_delete(self):
        self._deleted = True