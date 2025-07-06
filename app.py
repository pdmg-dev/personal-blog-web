from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret-key"

users = {"admin": generate_password_hash("admin1234")}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/article")
def article():
    return render_template("article.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and check_password_hash(users.get(username), password):
            flash("Login successfully.")
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials. Try again."

    return render_template("auth/login.html", error=error)


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add_article")
def add_article():
    return render_template("add_article.html")


if __name__ == "__main__":
    app.run(debug=True)
