from flask import Flask , request

app = Flask(__name__) # hum nai app mai flask ko as a object utha kr store kr diye

@app.route("/") # route bna rhe
def home():
    return "Hello Flask"


@app.route("/search")
# the function can be any name 
def search():
    name = request.args.get("name" ,"guest") # get method mai name ko get kr rhe ,,,,,, yha pr agar name na mile to guest ko default value kr diye
    return f"Hello {name}" # name ko return kr rhe

# Multiple query parmeter

@app.route("/search2")
def search2():
    name = request.args.get("name" ,"guest") # get method mai name ko get kr rhe ,,,,,, yha pr agar name na mile to guest ko default value kr diye
    location = request.args.get("location" ,"unknown") # get method mai location ko get kr rhe ,,,,,, yha pr agar location na mile to unknown ko default value kr diye
    return f"Hello {name} from {location}"
    



# multiple query parameter


if __name__=="__main__":
    app.run(debug=True) # automatic update krta rhe ga (debug=true) manuualy baar baar ruk kai start nhi krna padega