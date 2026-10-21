from flask import Flask , render_template , request , redirect , url_for , flash , session

app = Flask(__name__)


app.secret_key = "your_secret_key"  # Replace with a secure secret key for session management. secret_key is used to sign the session cookies to protect against cookie data tampering. It should be a random string and kept secret.it is used to encrypt the session data and ensure that it cannot be tampered with by the client. It is important to set a strong secret key to maintain the security of the application.it should be on environment variable or a config file and not hardcoded in the code for security reasons.

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404 # 404 is the HTTP status code for "Not Found". It indicates that the requested resource could not be found on the server. The second value in the return statement is the status code that will be sent back to the client along with the response. In this case, it is set to 404 to indicate that the page was not found.

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500 # 500 is the HTTP status code for "Internal Server Error". It indicates that an unexpected condition was encountered on the server, preventing it from fulfilling the request. The second value in the return statement is the status code that will be sent back to the client along with the response. In this case, it is set to 500 to indicate that there was an internal server error.

@app.route("/test-500")
def test_500():
    # This route is intentionally designed to raise an exception to test the 500 error handler.
    result = 1 / 0  # This will raise a ZeroDivisionError, triggering the 500 error handler.
    return str(result)
    
@app.route("/login")
def login():
    session["username"] = "Satyam"  # Set a session variable to indicate the user is logged in
    return "Logged successfully! <a href='/'>Go to Home</a>"

@app.route("/dashboard")
def dashboard():
    username = session.get("username")  # Retrieve the username from the session
    if not username:
        return "You are not logged in! <a href='/login'>Login</a>"
    return f"Welcome to the dashboard, {username}! <a href='/logout'>Logout</a>"

@app.route("/logout")
def logout():
    session.pop("username", None)  # Remove the username from the session to log out the user , none is used to avoid KeyError if the key doesn't exist simply it will return None if the key doesn't exist
    return "Logged out successfully! <a href='/'>Go to Home</a>"

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
    app.run(debug=True)  # Set debug to False for production. In production, you should set debug to False to prevent exposing sensitive information in error messages.