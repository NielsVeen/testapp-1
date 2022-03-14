from flask import Flask,request,jsonify,json
from database_function import database
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Homepage'

@app.route('/post',methods=['POST'])
def post():
    data = request.json

    # Create variables from request data
    submission_id = ['submit_id']
    email = data['email']
    cro_address = data['cro_address']
    ip_address = data['ip']

    # Run database function
    db = database(email,cro_address,ip_address,submission_id)

    if db == True:
        return 200

    return 'something went wrong'

if __name__ == '__main__':
    app.run(threaded=True,port=5000)