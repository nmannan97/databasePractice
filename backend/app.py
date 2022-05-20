from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 5000)

db = client.flask_db
todos = db.todos

@app.route('/hello')
def say_hello_world():
    return {'result': "Hello World"}