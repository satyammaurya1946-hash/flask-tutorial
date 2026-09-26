from flask import Flask

app = Flask(__name__) # hum nai app mai flask ko as a object utha kr store kr diye

@app.route("/") # route bna rhe
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "welcome to about page"

@app.route("/users")
def users():
    return "welcome to users page"


@app.route("/user/<name>")
def user(name):
    return f"hello {name}"

@app.route("/user/<name>/<course>")
def user(name, course):
    return f"hello {name}, you are enrolled in {course}"

if __name__=="__main__":
    app.run(debug=True) # automatic update krta rhe ga (debug=true) manuualy baar baar ruk kai start nhi krna padega