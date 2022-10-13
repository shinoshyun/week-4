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

    message = request.args.get("message", "")
    # 這是GET寫法，("message"代表網址後面的接的 EX:/error?message= , 後面的文字為預設文字(也可帶入數字))
    return render_template("error.html", message=message)
    # 後面的message可根據前端的message打了甚麼而做改變


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]  # 這是POST寫法，要把使用者在前端的資料抓進來後端，然後放進變數
    password = request.form["password"]

    if (account == "test") and (password == "test"):  # 如果說帳密都是test就回傳到(路由/member)
        return redirect("/member")

    elif (account == "") or (password == ""):

        # 任一欄為空 就導去(路由/error)先預設message後面的文字
        return redirect("/error?message=請輸入帳號、密碼")

    else:
        # 任一欄輸入錯的話就導去(路由/error)先預設message後面的文字
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route("/signout")
def signout():
    return redirect("/")


# -----------------------------------------------------

@app.route("/square")
def square():
    n = request.args.get("number")
    n = int(n)  # 上面那行帶入的數字會變成字串，所以要轉成變數int

    result = 0
    sum = n ** 2
    result += sum

    return render_template("result.html", sum=result)


app.run(port=3000)
