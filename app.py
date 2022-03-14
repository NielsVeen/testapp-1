from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Homepage'

@app.route('/post',methods=['POST'])
def post():
    data = request.form.get('text')
    return jsonify({'your_message': data})

if __name__ == '__main__':
    app.run(threaded=True,port=5000)