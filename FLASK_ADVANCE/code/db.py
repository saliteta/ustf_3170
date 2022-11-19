
import random
import string

# printing lowercase

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

ITEM_LIST = ['T-55', 'T62', 'T-72', 'T-90A', 'T-80', 'M1A1 AIM Abrams', 'Leopard 2A4', 'M60 A3 Patton', 'Type 59 Durjoy', 'Type 69',
'M-84', 'Type 59', 'Type 59', 'Type 88','Type 96','Type 99', 'Type 99A']




class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique = False)
    price = db.Column(db.Integer(), nullable=False, unique = False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique =False)

    def __repr__(self):
        return f'id: {self.id} name: {self.name} price:{self.price}'

def generate_random_Item(number = 10):
    item_list = []
    for i in range(number):
        rand_number = random.randint(0,len(ITEM_LIST)-1)
        letters = string.ascii_lowercase
        barcode = ( ''.join(random.choice(letters) for j in range(10)) )
        item = Item(name = ITEM_LIST[rand_number], price = random.randrange(1500000, 20000000), barcode = barcode, description = barcode)
        item_list.append(item)
    return item_list



if __name__ == '__main__':
    with app.app_context():
        #db.create_all()
        #for item in generate_random_Item():
        #    db.session.add(item)
        #    db.session.commit()
        #Item.query.all()
        items = Item.query.all()
        for item in items:
            print(item)