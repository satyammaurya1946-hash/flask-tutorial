from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)


@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    
    user = User(username=name, email=email, age=age)
    
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"})

@app.route("/get-users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "age": user.age
        }
        user_list.append(user_data)
    return jsonify(user_list)

@app.route("/get-user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user=db.get_or_404(User, user_id)
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "age": user.age
    }
    return jsonify(user_data)

@app.route("/")
def home():
    return "flask + sql alchemy + sqlite is working"

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
