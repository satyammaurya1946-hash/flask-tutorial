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
        name = request.form.get("name","").strip()
        email = request.form.get("email","").strip()
        age = request.form.get("age","").strip()
        # Process the form data (e.g., save to database,send email)
        if not name:
            return "Name is required"
        if not email:
            return "Email is required"
        if not age:
            return "Age is required"
        if not age.isdigit():
            return "Age must be a number"
        age = int(age)
        return "registration successful"
        
        # return render_template("contact.html", name=name, email=email, age=age)
    
    return render_template("contact.html")


if __name__=="__main__":
    app.run(debug=True)