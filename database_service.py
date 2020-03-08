import pyrebase
import json

with open('env/database_config.json', 'r') as config_file: config = json.load(config_file) 

firebase = pyrebase.initialize_app(config)

# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# default_app = firebase_admin.initialize_app()

db = firebase.database()
# data to save
data = {
    "user": {
        "name": "Mortimer Smith"
    }
}

# Pass the user's idToken to the push method
results = db.child("users").push(data)

print(results)