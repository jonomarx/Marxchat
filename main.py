from flask import Flask, request, Response, jsonify
import time, uuid, sys

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'squeek, squeek'

@app.route('/message/<username>', methods=['GET', 'POST'])

def squeek_message(username):
    if request.method == 'POST':
        msg_to=request.form['to']
        msg_from=request.form['from']
        msg=request.form['msg']
        raise Exception(msg_to, msg_from, msg)
        # print("hello world", file=sys.stderr)
        # return jsonify({'status': 'This is a POST message'})
    elif request.method == 'GET':
        return jsonify({'messages': [{'id':uuid.uuid4(), 'from':'dad', 'date':time.time(), 'msg': 'This is a test'}, {'id':uuid.uuid4(), 'from':'dad', 'date':time.time(), 'msg': 'test'}]})  




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"), debug=True)


