from flask import Flask, request, Response, jsonify
import time, json
from bson import ObjectId

# Initialize Mongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.messageDB
collection = db.message

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# Main 
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'squeek, squeek'

@app.route('/message/<username>', methods=['GET', 'POST'])

def squeek_message(username):
    if request.method == 'POST':
        json = request.json
        write(json)
        return JSONEncoder().encode(json)
    
    elif request.method == 'GET':
        return jsonify({'messages': [{'id':'id', 'from':'dad', 'date':time.time(), 'msg': 'This is a test'}, {'id':'id', 'from':'dad', 'date':time.time(), 'msg': 'test'}]})  

def write(message):
    message['time'] = str(time.time())
    messages = db.messages
    message_id = messages.insert_one(message).inserted_id
    message_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"), debug=True)


