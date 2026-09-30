from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    is_logged_in = False
    marks = 0
    return render_template("index.html",is_logged_in=is_logged_in,marks=marks)


if __name__=="__main__":
    app.run(debug=True) 