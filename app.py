from flask import Flask,request,jsonify,json
from database_function import database
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Homepage'

@app.route('/post',methods=['POST'])
def post():
    data = request.json
    message = data['text']
    answer = database(message)
    return jsonify({'your_message': answer})

if __name__ == '__main__':
    app.run(threaded=True,port=5000)