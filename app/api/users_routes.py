from flask import jsonify, request, Blueprint
from bson import ObjectId
from ..mongoDB import  users_collection
from .utils import make_serializable

user_routes = Blueprint('users', __name__)



@user_routes.route('', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        data = list(users_collection.find())
        return jsonify(make_serializable(data))  # Convert ObjectId to string before returning

    data = request.get_json()
    print('data from request ================> ', data)
    users_collection.insert_one(data)
    return jsonify({'message': 'User created successfully'})

@user_routes.route('/<string:_id>', methods=['PUT', 'DELETE'])
def handle_single_user(_id):
    print('id of the single user  ==== = = = >', _id)


    if request.method == 'DELETE':
        user = users_collection.find_one_and_delete({"_id": ObjectId(_id)})  # Use find_one() to get a single document

    if request.method == 'PUT':
        data = request.get_json()
        user = users_collection.find_one_and_replace({"_id": ObjectId(_id)}, data)  # Use find_one() to get a single document
        print('data ====> ', data)
        print('user ======> ', user)

    print('user detail from query ====> ', user)


    if user:
        user['_id'] = str(user['_id'])  # Convert the '_id' field to a string
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404
