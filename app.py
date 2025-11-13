from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/account")
def account():
	return "User account will be shown here"

@app.route("/page/<string:book_id>")
def page(book_id):
	return "This is where information about " + str(book_id) + " will be shown"

@app.route("/create_account")
def create_account():
	return render_template("create_account.html")

@app.route("/signin")
def signin():
	return render_template("signin.html")

@app.route("/result", methods=["POST"])
def result():
	message = request.form["message"]
	return render_template("result.html", message=message)

@app.route("/page2")
def page2():
	return "Toinen sivu"
