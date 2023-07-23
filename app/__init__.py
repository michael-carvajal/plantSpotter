from flask import Flask
from .api.users_routes import user_routes
from .api.plants_routes import plants_routes


app = Flask(__name__)


app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(plants_routes, url_prefix='/api/plants')

if __name__ == '__main__':
    app.run(debug=True)




# example route
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     print('inside route')
#     data = list(db.my_collection.find())
#     return jsonify(data)
