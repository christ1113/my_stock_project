from flask import Blueprint, jsonify

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the backend API!"})

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify({"message": "Login route is working."})
