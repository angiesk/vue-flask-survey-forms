from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'survey'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/survey'
mongo = PyMongo(app)

CORS(app)

@app.route('/')
def hello():
    return('<h1>Hello World</h1>')



if __name__ == '__main__':
    app.run(debug=True)
