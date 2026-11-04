from flask import Flask
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

@app.route('/')
def home():
    return "Hello, Flask with MySQL!"

@app.route('/test_db')
def test_db():
    result = db.session.execute(text("SELECT 1"))
    value = result.scalar() # this line reads the result of sql
    return f"Database connection test successful! Result: {value}"

if __name__ == '__main__':
    app.run(debug=True)
