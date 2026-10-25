from flask import Flask , render_template , request , redirect , url_for , flash , session 
import os
from dotenv import load_dotenv
from users.routes import users_bp
from products.routes import products_bp

load_dotenv()  # Load environment variables from a .env file if present. This allows you to keep sensitive information like secret keys and configuration settings outside of your codebase, enhancing security and flexibility.

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

@app.route("/")
def home():
    return "home page"

if __name__=="__main__":
    app.run(debug=True)  # Set debug to False for production. In production, you should set debug to False to prevent exposing sensitive information in error messages.