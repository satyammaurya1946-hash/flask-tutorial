from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    name="rohit"
    course="B.tech"
    city = "delhi"
    return render_template("index.html",name=name,course=course,city=city)


if __name__=="__main__":
    app.run(debug=True) 