from importlib.resources import path
import random
import string
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(200), nullable=False)
    path = db.Column(db.String(6), nullable=False)

@app.route("/", methods=["POST","GET"])
def shorten():
    if request.method == "POST":

        #URL validate
        destination = request.form["url"]
        if("www." in destination):
            destination = f'https://{destination}/'
            print(destination)
        elif ("https://" not in destination and "http://" not in destination):
            destination = f'https://www.{destination}/'

        #check if url is active
        try:
            requests.get(url = destination)
        except:
            #render error on page
            return "error"
        
        #check if the url is already in the database
        path = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=6))
    else:
        return render_template("index.html")

@app.route("/expand", methods=["POST","GET"])
def expand():
    if request.method == "POST":

        #URL validate
        url = request.form["url"]
        if("www." in url):
            url = f'http://{url}/'
        elif ("https://" not in url and "http://" not in url):
            url = f'http://www.{url}/'
        
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


@app.route("/<path>")
def forward(path):
    return redirect("http://google.de")

if __name__ == "__main__":
    app.run(debug=True)