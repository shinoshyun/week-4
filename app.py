from email import message
import numbers
from unittest import result
from flask import Flask, request, render_template, session, redirect


app = Flask(__name__, static_folder="static",
            static_url_path="/")  # __name__ 代表目前執行的模組

app.secret_key = "any string but secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/member")
def member():
    return render_template("member.html")


@app.route("/error")
def error():
    message = request.args.get("message", "帳號、或密碼輸入錯誤")
    return render_template("error.html", message=message)


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]  # 要把使用者在前端的資料抓進來後端，這是POST寫法，然後放進變數
    password = request.form["password"]

    if (account == "test") and (password == "test"):  # 如果說帳密都是test就回傳到/member
        return redirect("/member")

    elif (account == "") or (password == ""):

        return redirect("/error")  # 錯的話就導去error

    else:
        return redirect("/error")


@app.route("/signout")
def signout():
    return redirect("/")


# -----------------------------------------------------

@app.route("/square")
def square():
    n = request.args.get("number")
    n = int(n)

    result = 0
    sum = n ** 2
    result += sum

    return render_template("result.html", sum=result)


app.run(port=3000)
