from flask import Flask, request
from flask import send_from_directory
import json
import firebase_admin
from firebase_admin import firestore


import os
os.environ['GRPC_DNS_RESOLVER'] = 'native'

firebase_app = firebase_admin.initialize_app(options={'projectId': "[PROJECT_ID]"})
db = firestore.client()

app = Flask(__name__)

@app.route('/api', methods=["GET"])
def get_books():
    doc_ref = db.collection(u'bootstrap').document(u'helloworld')
    doc = doc_ref.get()

    return doc.to_dict()["message"];

@app.route('/api', methods=["POST"])
def post_book():
    data = json.loads(request.data)
    col_ref = db.collection(u'bootstrap')
    doc = col_ref.add(data)

    return doc;

@app.route('/books/<id>', methods=["PATCH"])
def patch_book(id):
    books_ref = db.collection(u'bootstrap')
    doc = books_ref.document(id)
    data = json.loads(request.data)
    doc.set(data)
    return data 

@app.route('/books/<id>', methods=["DELETE"])
def remove_book(id):
    books_ref = db.collection(u'bootstrap')
    doc = books_ref.document(id)
    doc.delete()
    return {"result": 200}


@app.route('/')
def index():
    return send_from_directory("build", "index.html")

@app.route('/<path:path>')
def frontend(path):
    return send_from_directory("build", path)

if __name__ == '__main__':
    from flask_cors import CORS
    CORS(app)
    app.run(host='127.0.0.1', port=8080, debug=True)
