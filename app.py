from flask import Flask
from uuid import UUID

app = Flask(__name__) # hum nai app mai flask ko as a object utha kr store kr diye

@app.route("/") # route bna rhe
def home():
    return "Hello Flask"

@app.route("/user/<int:id>") # route bna rhe, <int:id> ka mtlb ye hai ki user ke baad jo bhi number aayega wo id mai store ho jaayega
def user(id):
    return f"User id is {id}"

@app.route("/price/<float:price>") # route bna rhe, <float:price> ka mtlb ye hai ki price ke baad jo bhi number aayega wo price mai store ho jaayega
def price(price):
    return f"Price is {price}"

@app.route("/name/<string:name>") # route bna rhe, <string:name> ka mtlb ye hai ki name ke baad jo bhi string aayega wo name mai store ho jaayega
def name(name):
    return f"Name is {name}"

@app.route("/path/<path:path>") # route bna rhe, <path:path> ka mtlb ye hai ki path ke baad jo bhi path aayega wo path mai store ho jaayega
def path(path):
    return f"Path is {path}"

@app.route("/student/<uuid:user_id>") # route bna rhe, <uuid:user_id> ka mtlb ye hai ki student ke baad jo bhi uuid aayega wo user_id mai store ho jaayega
def stu(user_id):
    return f"Student id is {user_id}"
if __name__=="__main__":
    app.run(debug=True) # automatic update krta rhe ga (debug=true) manuualy baar baar ruk kai start nhi krna padega