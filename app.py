from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret-key"


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
        if (
            request.form["username"] != "admin"
            or request.form["password"] != "admin1234"
        ):
            error = "Invalid credentials. Try again."
        else:
            flash("Login successfully.")
            return redirect(url_for("dashboard"))

    return render_template("auth/login.html", error=error)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
