from importlib.resources import path
import random
import string
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

# constants
PATH_LENGTH = 6
# maximum (official) length of a URL according to www.sistrix.com/ask-sistrix/technical-seo/site-structure/url-length-how-long-can-a-url-be
MAX_URL_LENGTH = 2048

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(MAX_URL_LENGTH), nullable=False)
    path = db.Column(db.String(PATH_LENGTH), nullable=False)

@app.route("/", methods=["POST","GET"])
def shorten():
    if request.method == "POST":

        #URL validate
        destination = validatedUrl(request.form["url"])

        #check if url is active
        try:
            requests.get(url = destination)
        except:
            #render error on page
            return render_template("index.html", error=True, url=destination)
        
        #check if the url is already in the database
        path = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=PATH_LENGTH))
    else:
        return render_template("index.html")

@app.route("/expand", methods=["POST","GET"])
def expand():
    if request.method == "POST":

        #URL validate
        url = validatedUrl(request.form["url"])
        
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


def validatedUrl(url):
    if ("https://" not in url and "http://" not in url):
        return f'http://{url}/'
    return url

if __name__ == "__main__":
    app.run(debug=True)