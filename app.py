from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__, static_folder="public",
            static_url_path="/")  # __name__ 代表目前執行的模組


@app.route("/")
def index():
    return render_template("index.html")


app.run(port=3000)
