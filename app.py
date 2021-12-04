from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mission_to_mars
mars = db.mars


@app.route("/scrape")
def scraper():
    listings = client.db.listings
    listings_data = scrape_mars.scrape()
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


@app.route("/")
def index():
    listings = client.db.listings.find_one()
    return render_template("index.html", listings=listings)




if __name__ == "__main__":
    app.run(debug=True)
