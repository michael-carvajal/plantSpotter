def make_serializable(data):
    # Convert ObjectId to string representation in the '_id' field
    for item in data:
        item['_id'] = str(item['_id'])
    return data
