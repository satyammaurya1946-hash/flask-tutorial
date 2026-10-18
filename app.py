from flask import Flask , render_template , request , redirect , url_for , flash

app = Flask(__name__)


app.secret_key = "your_secret_key"  # Replace with a secure secret key for session management
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
            flash("Name is required!","danger")
            return redirect(url_for("contact"))
        if not email:
            flash("email is required!","danger")
            return redirect(url_for("contact"))
        if not age:
            flash("age is required!","danger")
            return redirect(url_for("contact"))
        if not age.isdigit():
            return "Age must be a number"
        # age = int(age)
        # return redirect("/success")
        # return redirect(url_for("success"))
        flash("Form submitted successfully!","success")
        
        # return render_template("contact.html", name=name, email=email, age=age)
    
    return render_template("contact.html")

@app.route("/success")
def success():
    return "Form submitted successfully!"

if __name__=="__main__":
    app.run(debug=True)