from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

@app.route("/")
def shorten():
    return render_template("index.html")

@app.route("/expand", methods=["POST","GET"])
def expand():
    if request.method == "POST":
        #Make http request and grab url header
        url = request.form["url"]
        response = requests.get(url = url)
        print(response.url)
        return "test"
    else:
        return render_template("expand.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)