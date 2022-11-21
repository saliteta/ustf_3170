# COME TO THE TUTORIAL IF YOU DO NOT UNDERSTAND
# COME TO THE TUTORIAL IF YOU DO NOT UNDERSTAND
# COME TO THE TUTORIAL IF YOU DO NOT UNDERSTAND


# FLASK CLASS & FUNCTION INTRODUCTION

## Flask()
- This is a class can be import from flask
- It will generate a flask render environment according to the variable you passed
- Following code means pass the name of your python file and make it rendered by Flask engine. "app" will be the flask environment to use
```
from flask import Flask
app = Flask(__name__)
```

## render_template()
- This is a function can be import from flask
- This funtion can be used to return a html file
- HTML file should be displayed in under the Flask environment
- Use decorator to specify the route you want to access
- Following content give you an example: You can access your html by type in ip_address:port_number/ to see your_html you can access your_html_aha by type in ip_address:port_number/aha
```
@app.route('/')
def home_page():
  return render_template('your_html.html')

@app.route('/aha')
def home_page_aha():
  return render_template('your_html_aha.html')
```





# Import Template from BootStrap
- Download all the codes in the templates folder
- By modifying the content in the html, we can have our own pages


# Jinja Syntax
- Jinja Syntax can deal with the problem of how to transfer the data from python to html
- The following code is an example for passing argument from python side
```
  item = 'saliteta'
  return render_template('your_html.html', item=item)
```
- The following code is an example for reciving argument from html side (using Jinja), display saliteta on html
```
  <p>{{ item }}</p>
```

## More Jinja Syntax
- For
```
  {% for item in items %}
```
- HTML temolates Hierachy
```
  {% block (key name you pass from another templates) %}
  {% endblock %}
```  

# Connect to Database
## Install Repo
- Database name: SQlite3(lite version of MySQL)
- Install modified Flask module to connect to SQlite3
- In your terminal type in the following command
```
  pip install flask-sqlalchemy
```

## flask-sqlalchemy Introduction
- app.config:
app is a Flask class, app.config is a dictionary. To use database set one element of this to the path you want

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
```

- SQLAlchemy:
It is a class that represent a database use the SQLite3
```
  db = SQLAlchemy(app)
```


- Create a Table in one database
One must inherit from your_database.Model
```
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique = False)
    price = db.Column(db.Integer(), nullable=False, unique = False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique =False)
```

- Create Database Intance and Add Item to your database:
```
  with app.app_context():
        db.create_all()
        for item in generate_random_Item():
            db.session.add(item)
            db.session.commit()
        Item.query.all()
        items = Item.query.all()
        for item in items:
            print(item)
```

# Terminal SQLITE3

```
sudo apt update
sudo apt upgrade
sudo apt install sqlite3
sqlite3 –version
sudo apt update
sudo apt install sqlitebrowser
```

 
