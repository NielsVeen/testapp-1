from flask import Flask,request,jsonify,json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Homepage'

@app.route('/post',methods=['POST'])
def post():
    data = request.json
    message = data['text']
    return jsonify({'your_message': message})

if __name__ == '__main__':
    app.run(threaded=True,port=5000)