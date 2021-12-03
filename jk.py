import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
val = input("Enter your email: ")
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

result = db.collection('hospitals').document(val).get()

if result.exists:
    print(result.to_dict())


