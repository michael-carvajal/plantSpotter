from flask import jsonify, request, Blueprint
from bson import ObjectId
from ..mongoDB import  plants_collection

plants_routes = Blueprint('plants', __name__)


