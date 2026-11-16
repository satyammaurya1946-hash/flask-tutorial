from flask import Flask , request, jsonify
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

client.admin.command('ping')
print("Connected to MongoDB!")

db = client['flask_db']
user_collection = db['users']

@app.route('/')
def home():
    return "Hello, Flask with MongoDB!"

@app.route('/user')
def create_user():
    user = {
        "name": "satyam",
        "email": "satyam@example.com"
    }
    result = user_collection.insert_one(user)
    return jsonify({"message": "User created successfully!",
                    "id": str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True)
