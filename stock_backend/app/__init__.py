from flask import Flask
from .config import Config
from .extensions import db
from .routes import auth_bp  # 引入帳號相關的路由
from flask_cors import CORS  # 加入 CORS

def create_app():
    app = Flask(__name__)
    
    # 載入設定
    app.config.from_object(Config)
    
    # 初始化資料庫
    db.init_app(app)


    # 啟用 CORS，允許前端的請求
    CORS(app, resources={r"/*": {"origins": "*"}})

    # 註冊藍圖
    app.register_blueprint(auth_bp, url_prefix='/auth')
    # app.register_blueprint(user_bp, url_prefix='/user')

    # 確保資料表建立
    with app.app_context():
        db.create_all()

    return app