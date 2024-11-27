from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.user_service import UsersService

# Create a Blueprint
bp = Blueprint('main', __name__)

# Instantiate UsersService singleton
users_service = UsersService()

@bp.route('/', methods=['GET'])
@jwt_required()
def hello_world():
    return 'Hello, World!'

@bp.route('/api/login/', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if not email or not password:
        return jsonify({'message': 'Invalid credentials'}), 401

    response_data, status_code = users_service.login(email, password)
    return jsonify(response_data), status_code
