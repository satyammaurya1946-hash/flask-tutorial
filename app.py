from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    # name = None
    if request.method == "POST":
        name = request.form.get("username")
        email = request.form.get("email")
        message = request.form.get("message")
        # Process the form data (e.g., save to database, send email)
        return render_template("contact.html", name=name, email=email, message=message)
    
    return render_template("contact.html")


if __name__=="__main__":
    app.run(debug=True) 