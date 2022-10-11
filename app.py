from cgitb import text
from importlib.resources import path
from tkinter.ttk import Style
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__, static_folder="static",
            static_url_path="/")  # __name__ 代表目前執行的模組


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/member")
def member():
    account = request.args.get("account")

    # if account == "test"

    return render_template("member.html")


app.run(port=3000)
