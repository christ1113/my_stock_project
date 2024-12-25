from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 使用者列表 (user_list)
class User(db.Model):
    __tablename__ = 'user_list'
    user_id = db.Column(db.Integer, primary_key=True)
    user_account = db.Column(db.String(50), unique=True, nullable=False)
    user_password = db.Column(db.String(256), nullable=False)

# 股票列表 (stock_list)
class Stock(db.Model):
    __tablename__ = 'stock_list'
    stock_id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String(10), nullable=False)
    stock_name = db.Column(db.String(100), nullable=False)

# 股票收藏列表 (user_stock)
class UserStock(db.Model):
    __tablename__ = 'user_stock'
    user_id = db.Column(db.Integer, db.ForeignKey('user_list.user_id'), primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock_list.stock_id'), primary_key=True)
    add_time = db.Column(db.DateTime, nullable=False)
