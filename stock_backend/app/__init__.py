from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    
    # SQLite 資料庫設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../stock.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化資料庫
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
