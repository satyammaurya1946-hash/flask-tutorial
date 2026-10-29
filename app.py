from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "flask + sql alchemy + sqlite is working"

if __name__=="__main__":
    app.run(debug=True)  