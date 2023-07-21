from flask import Flask, jsonify, request, Blueprint
from .api.users_routes import user_routes


app = Flask(__name__)


app.register_blueprint(user_routes, url_prefix='/api/users')
# example route
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     print('inside route')
#     data = list(db.my_collection.find())
#     return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
