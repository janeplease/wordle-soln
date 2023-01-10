from be import app
from flask import request

@app.route("/postcodedword/<name>", methods = ['POST'])
def get_coded_word():
    name = request.args.get('name')
    print(name)


@app.route("/getnewword", methods = ['GET'])
def send_new_word():
    return "Hello, Flask!!!!!!"


@app.route("/getnewword1", methods = ['GET'])
def send_new_word1():
    return "Hello, Flask!!!!!!"


@app.route("/post1", methods = ['POST'])
def get_coded_word1():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'