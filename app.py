from flask import Flask , request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

client.admin.command('ping')
print("Connected to MongoDB!")

db = client['flask_db']
user_collection = db['users']

@app.route('/')
def home():
    return "Hello, Flask with MongoDB!"

# insert a single user

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    result = user_collection.insert_one(data)
    return jsonify({"message": "User created successfully!",
                    "id": str(result.inserted_id)}), 201

# insert multiple users

@app.route("/users/bulk", methods=["POST"])
def create_user_bulk():
    data = request.get_json()
    result = user_collection.insert_many(data)
    ids = [str(id) for id in result.inserted_ids]
    return jsonify({"message": "Users created successfully!",
                    "ids": ids}), 201
    
# reads all users

@app.route("/users", methods=["GET"])
def get_users():
    users = user_collection.find()
    users_data = []
    for user in users:
        users_data.append({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "age": user["age"]
        })
    return jsonify({"users": users_data}), 200

# reads a single user by id

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"]
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
