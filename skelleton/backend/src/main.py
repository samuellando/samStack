from flask import Flask, request, abort
from flask import send_from_directory
import json
import anyrest
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

@app.route('/api/example', methods=['GET'])
def example():
    '''
    Example endpoint.
    '''
    data = json.loads(request.data)
    args = request.args
    if data.get('abort'):
        abort(400)
    return ar.get('example')

@app.route('/')
def index():
    '''
    Serves the frontend home page.
    '''
    return send_from_directory("../../build", "index.html")

@app.route('/<path:path>')
def frontend(path):
    '''
    Serves the frontend.
    '''
    try:
        return send_from_directory("../../build", path)
    except:
        return send_from_directory("../../build", path+".html")

import os
authority=None
audience=None
lockApi=False

if "MONGODB_USER" in os.environ and "MONGODB_PASSWORD" in os.environ and "MONGODB_HOST" in os.environ and "MONGODB_DATABASE" in os.environ:
    uri = "mongodb+srv://{}:{}@{}/?retryWrites=true&w=majority".format(os.environ["MONGODB_USER"], os.environ["MONGODB_PASSWORD"], os.environ["MONGODB_HOST"])
    client = MongoClient(uri,
                         tls=True,
                         server_api=ServerApi('1'))
    db = client[os.environ["MONGODB_DATABASE"]]
    ar = anyrest.addAnyrestHandlersMongoDB(app, db, authority, audience, lockApi)
else:
    uri = ""
    print("The following environment variables are required: MONGODB_USER, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_DATABASE")
    print("Using testing backend database.")
    ar = anyrest.addAnyrestHandlersTesting(app)

if __name__ == '__main__':
    from flask_cors import CORS
    CORS(app)
    app.run(host='127.0.0.1', port=8080, debug=True)
