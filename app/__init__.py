from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)

# Replace 'my_mongodb_uri' with the actual URI for your MongoDB database
# For example: 'mongodb://localhost:27017/my_database'
mongo_uri = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1'
client = MongoClient(mongo_uri)
db = client.my_database   # Change 'my_database' to your desired database name
users_collection = db.users

def make_serializable(data):
    # Convert ObjectId to string representation in the '_id' field
    for item in data:
        item['_id'] = str(item['_id'])
    return data

@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        data = list(users_collection.find())
        return jsonify(make_serializable(data))  # Convert ObjectId to string before returning

    data = request.get_json()
    print('data from request ================> ', data)
    users_collection.insert_one(data)
    return jsonify({'message': 'User created successfully'})

@app.route('/api/users/<string:_id>', methods=['PUT', 'DELETE'])
def handle_single_user(_id):
    print('id of the single user  ==== = = = >', _id)
    user = users_collection.find_one_and_delete({"_id": ObjectId(_id)})  # Use find_one() to get a single document
    print('user detail from query ====> ', user)
    if user:
        user['_id'] = str(user['_id'])  # Convert the '_id' field to a string
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/api/data', methods=['GET'])
def get_data():
    print('inside route')
    data = list(db.my_collection.find())
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
