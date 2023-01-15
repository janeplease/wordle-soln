
from be import app
from flask import request
from be.services.output_from_sevice import OutputFromService


outputFromService = OutputFromService


@app.route("/startsession", methods = ['GET'])
def start_session():
    outputFromService.initialize_session(outputFromService)
    return "Session started"


@app.route("/getnewword", methods = ['GET'])
def get_new_word():
    return outputFromService.get_suggested_word(outputFromService)


@app.route("/setresultfromgame", methods = ['POST'])
def get_coded_word1():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        interpreted_word = json['interpreted_word']
        outputFromService.set_result_from_game(outputFromService, interpreted_word=interpreted_word)
        return 'Interpreted word received'
    else:
        return 'Content-Type not supported!'


@app.route("/closesession", methods = ['GET'])
def close_session():
    outputFromService.close_session(outputFromService)
    return "Session closed"



# @app.route("/postcodedword/<name>", methods = ['POST'])
# def get_coded_word():
#     name = request.args.get('name')
#     print(name)


# @app.route("/getnewword", methods = ['GET'])
# def get_new_word():
#     return "Hello, Flask!!!!!!"


# @app.route("/getnewword1", methods = ['GET'])
# def send_new_word1():
#     return "Hello, Flask!!!!!!"


# @app.route("/post1", methods = ['POST'])
# def get_coded_word1():
#     content_type = request.headers.get('Content-Type')
#     if (content_type == 'application/json'):
#         json = request.json
#         return json
#     else:
#         return 'Content-Type not supported!'