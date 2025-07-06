from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "secret-key"

users = {"admin": generate_password_hash("admin1234")}


@app.route("/")
def home():
    return render_template("guest/home.html")


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
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials. Try again."

    return render_template("auth/login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("admin/dashboard.html")
    return redirect(url_for("login"))


@app.route("/new-article")
def add_article():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("admin/add_article.html")


if __name__ == "__main__":
    app.run(debug=True)
