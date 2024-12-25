from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
import subprocess


app = Flask(__name__)


mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["twitter_scraper"]
collection = db["trending_topics"]

@app.route("/")
def index():
    """Display trending topics fetched from MongoDB."""
    trending_data = collection.find_one(sort=[("_id", -1)])
    trending_topics = []
    if trending_data:
        trending_topics = [
            trending_data.get("trend1", "N/A"),
            trending_data.get("trend2", "N/A"),
            trending_data.get("trend3", "N/A"),
            trending_data.get("trend4", "N/A"),
        ]
        timestamp = trending_data.get("timestamp", "Unknown Time")
    return render_template("index.html", trending_topics=trending_topics, timestamp=timestamp)

@app.route("/run-script")
def run_script():
    """Run the Selenium script and then redirect to the home page."""
    try:
        subprocess.run(["python3", "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the script: {e}")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
