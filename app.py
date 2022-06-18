from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

@app.route("/")
def shorten():
    return render_template("index.html")

@app.route("/expand", methods=["POST","GET"])
def expand():
    if request.method == "POST":

        #URL validate
        url = request.form["url"]
        if("www." in url):
            url = f'https://{url}/'
            print(url)
        elif ("https://" not in url):
            url = f'https://www.{url}/'
        
        #make http request
        try:
            response = requests.get(url = url)
            return render_template("expand.html", response = response.url, url=url)
        except:
            return render_template("expand.html", url=url)
    else:
        return render_template("expand.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)