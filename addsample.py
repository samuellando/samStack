import sys
import firebase_admin
from firebase_admin import firestore
import anyrest

import os
os.environ['GRPC_DNS_RESOLVER'] = 'native'

import sys 
project = sys.argv[1]


firebase_app = firebase_admin.initialize_app(options={'projectId': project})
db = firestore.client()

anyrest.insert_data_into_firestore({"message": "Hello, World!"}, db.collection("helloworld").document("sampledocument"))
