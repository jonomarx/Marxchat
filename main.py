from flask import Flask, request, Response, jsonify
import time, uuid, sys

# Initialize Mongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.messageDB
collection = db.message

# Main 
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'squeek, squeek'

@app.route('/message/<username>', methods=['GET', 'POST'])

def squeek_message(username):
    if request.method == 'POST':
        write(request.json)
        return 
        # return jsonify({'Message ID': 'OK'})
    
    elif request.method == 'GET':
        return jsonify({'messages': [{'id':uuid.uuid4(), 'from':'dad', 'date':time.time(), 'msg': 'This is a test'}, {'id':uuid.uuid4(), 'from':'dad', 'date':time.time(), 'msg': 'test'}]})  

def write(post):
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    post_id
    return post_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"), debug=True)


