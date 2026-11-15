from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
# Configure the database connection using environment variables
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = quote_plus(os.getenv('DB_PASSWORD'))
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    orders = db.relationship("Order",backref="user",lazy=True)
    # here order is reffere the model class name Order

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # user_id -----> users.id
    
@app.route('/')
def home():
    return "Hello, Flask with MySQL!"

@app.route("/users",methods=["POST"])
def create_user():
    data = request.get_json()
    # new_user = user(name=data['name'], email=data['email'], age=data['age']) # this is also correct but if we want to handle the case where some fields might be missing, we can use the get method
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    new_user = User(name=name, email=email, age=age)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!",
                   "user id": new_user.id}), 201
    
    
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    product = data.get("product")
    amount = data.get("amount")
    user_id = data.get("user_id")

    order = Order(product=product, amount=amount, user_id=user_id)
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created successfully!",
                    "order id": order.id})


@app.route("/users/<int:user_id>/orders", methods=["GET"])
def get_user_orders(user_id):
    user = db.get_or_404(User, user_id)
    orders = user.orders  # Access the related orders using the relationship
    orders_data = []
    for order in orders:
        orders_data.append({
            "id": order.id,
            "product": order.product,
            "amount": order.amount
        })
    return jsonify({"user": user.name,
                    "orders": orders_data}), 200


@app.route("/users/filter", methods=["GET"])
def filter_users():
    age = request.args.get("age", type=int)
    if age is None:
        return jsonify({"error": "Age parameter is required"}), 400
    
    users = User.query.filter(User.age >= age).all()
    users_data = []
    for user in users:
        users_data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        })
    return jsonify({"users": users_data}), 200

# @app.route("/users/orders", methods=["GET"])
# def user_orders():
#     sql = text("""
#         SELECT users.id AS user_id, users.name AS user_name, users.email AS user_email, users.age AS user_age,
#                orders.id AS order_id, orders.product AS order_product, orders.amount AS order_amount
#         FROM users
#         LEFT JOIN orders ON users.id = orders.user_id
#     """)
#     result = db.session.execute(sql)
#     data = []
#     for row in result:
#         data.append({
#             "user_id": row.user_id,
#             "user_name": row.user_name,
#             "user_email": row.user_email,
#             "user_age": row.user_age,
#             "order_id": row.order_id,
#             "order_product": row.order_product,
#             "order_amount": row.order_amount
#         })
#     return jsonify(data), 200

@app.route("/users/orders", methods=["GET"])
def user_orders():
    result = db.session.query(User.name,Order.product,Order.amount).join(Order, User.id == Order.user_id)
    data = []
    for name, product, amount in result:
        data.append({
            "user_name": name,
            "product": product,
            "amount": amount
        })
    return jsonify(data), 200

@app.route("/users", methods=["GET"])
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 2, type=int)
    pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)
    users = pagination.items
    users_data = []
    for user in users:
        users_data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        })
    return jsonify({"users": users_data}), 200


if __name__ == '__main__':
    with app.app_context():
        # Create the database tables if they don't exist
        db.create_all()
    app.run(debug=True)
