from flask import Flask, request, Response, jsonify
import time, json
from bson import ObjectId

# Initialize Mongo
from pymongo import MongoClient
client = MongoClient('mongodb://python:py1234@ds056688.mlab.com:56688/messagedb')
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
        json = request.form
        write(json)
        return JSONEncoder().encode(json)
    
    elif request.method == 'GET':
        cursor = db.messages.find({"to": username})
        messages = []
        for i in cursor:
            messages.append(i)
            i["_id"] = str(i["_id"])
        return jsonify({"messages": messages})
    
def write(message):
    message = dict(message)
    message['time'] = str(time.time())
    messages = db.messages
    message_id = messages.insert_one(message).inserted_id
    message_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"), debug=True)


