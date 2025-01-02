from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from extensions import db

# 用戶註冊邏輯
def register_user(data):
    user_account = data.get('user_account')
    user_password = data.get('user_password')
    
    if User.query.filter_by(user_account=user_account).first():
        return {"msg": "Registration failed"}, 400
    
    hashed_password = generate_password_hash(user_password)
    new_user = User(user_account=user_account, user_password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return {"msg": "User created successfully"}, 201

# 用戶驗證（登入邏輯）
def authenticate_user(data):
    user_account = data.get('user_account')
    user_password = data.get('user_password')
    
    user = User.query.filter_by(user_account=user_account).first()
    
    if user and check_password_hash(user.user_password, user_password):
        return user
    return None
