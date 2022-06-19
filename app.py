from importlib.resources import path
from flask import Flask, render_template, request
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

    #URL validate
    url = request.form["url"]
    if("www." in url):
        url = f'https://{url}/'
        print(url)
    elif ("https://" not in url):
        url = f'https://www.{url}/'
    
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