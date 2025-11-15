from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/account")
def account():
	return "User account will be shown here"

@app.route("/create_post")
def create_post():
	return render_template("create_post.html")

@app.route("/book/<string:book_id>")
def book(book_id):
	return "This is where information about " + str(book_id) + " will be shown"

@app.route("/create_account")
def create_account():
	return render_template("create_account.html")

@app.route("/signin")
def signin():
	return render_template("signin.html")

@app.route("/account", methods=["POST"])
def result():
	message = request.form["message"]
	return render_template("account.html", message=message)
