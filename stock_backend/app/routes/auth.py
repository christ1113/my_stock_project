from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from service.auth_service import register_user, authenticate_user

auth_bp = Blueprint('auth_bp', __name__)

# 註冊用戶
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    result = register_user(data)
    return jsonify(result['msg']), result['status']

# 登入並發送 JWT
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate_user(data)
    
    if user:
        access_token = create_access_token(identity=user.user_id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401
