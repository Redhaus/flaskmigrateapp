from flask import Flask

# import sqlalchemy and flask migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# create uri string for sql alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iurktrofgpsvyf:8f584f435b40b9cd0080d2208f38fecf7fcf743c5ba1bb9976bc9b3ef5599799@ec2-174-129-32-230.compute-1.amazonaws.com:5432/d2otbprt3gi5b5'

# create db object from sqlalchemy give it app
db = SQLAlchemy(app)
# create migrate obj and give it app and db
migrate = Migrate(app, db)

# create a simple model to test it out
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    subscribed = db.Column(db.Boolean)
    questions = db.Column(db.ARRAY(db.String()))

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
