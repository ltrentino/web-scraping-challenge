from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# connect to mongo db and collection



@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
