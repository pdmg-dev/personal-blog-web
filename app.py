from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from storage import save_article, update_article
from utils import get_articles, get_current_date, get_article_filepath

from markdown import markdown

import os

app = Flask(__name__)
app.secret_key = "secret-key"

users = {"admin": generate_password_hash("admin1234")}


# Home route (GUEST)
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("guest/home.html", articles=get_articles())


# Article route (GUEST)
@app.route("/article/<slug>")
def view_article(slug):
    article = get_articles(slug)
    article["content"] = markdown(article["content"])
    return render_template("guest/view_article.html", article=article)


# Login route
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


# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


# Dashboard route (ADMIN)
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("admin/dashboard.html", articles=get_articles())
    return redirect(url_for("login"))


# New Article (ADMIN)
@app.route("/new-article", methods=["GET", "POST"])
def add_article():
    current_date = get_current_date()
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        date_published = request.form["date_published"]
        content = request.form["content"]

        save_article(title, date_published, content)
        flash("Article successfully published.")
        return redirect(url_for("dashboard"))

    return render_template("admin/add_article.html", current_date=current_date)


# Edit route
@app.route("/edit-article/<slug>", methods=["GET", "POST"])
def edit_article(slug):
    article = get_articles(slug)

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        date_published = request.form["date_published"]
        content = request.form["content"]

        update_article(title, date_published, content, slug)
        flash("Article successfully updated.")

        return redirect(url_for("dashboard"))
    return render_template("/admin/edit_article.html", article=article)


# Delete route
@app.route("/delete-article/<slug>")
def delete_article(slug):
    if "username" not in session:
        return redirect(url_for("login"))

    filepath = get_article_filepath(slug)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash("Article successfully deleted.")
    else:
        flash("Article not found.")

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
