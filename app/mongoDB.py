from pymongo import MongoClient


# Replace 'my_mongodb_uri' with the actual URI for your MongoDB database
# For example: 'mongodb://localhost:27017/my_database'

mongo_uri = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1'
client = MongoClient(mongo_uri)
db = client.my_database   # Change 'my_database' to your desired database name

def make_serializable(data):
    # Convert ObjectId to string representation in the '_id' field
    for item in data:
        item['_id'] = str(item['_id'])
    return data



users_collection = db.users
