from flask import Flask

app = Flask(__name__) # hum nai app mai flask ko as a object utha kr store kr diye

@app.route("/") # route bna rhe
def home():
    return "Hello Flask"

if __name__=="__main__":
    app.run(debug=True) # automatic update krta rhe ga (debug=true) manuualy baar baar ruk kai start nhi krna padega