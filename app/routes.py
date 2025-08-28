from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sum", methods=["POST"])
def sum_numbers():
    try:
        a = float(request.form.get("a", 0))
        b = float(request.form.get("b", 0))
        result = a + b
        return render_template("index.html", result=result, a=a, b=b)
    except ValueError:
        return render_template("index.html", error="Invalid input")
