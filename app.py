from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses =["python","java","Flask","Django"]
    student = {"name":"John","age":22,"course":"python"}
    return render_template("index.html", courses=courses, student=student)


if __name__=="__main__":
    app.run(debug=True) 