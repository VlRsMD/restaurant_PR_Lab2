from flask import Flask, request

restaurant = Flask(__name__)

@restaurant.route('/post', methods = ['POST'])
def post():
    req = request.json
    return req

@restaurant.route('/get', methods = ['GET'])
def get():
    req = request.json
    return req

if __name__ == '__main__':
    restaurant.run(host='127.0.0.1', port=3900)
