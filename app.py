# Dependencies
from flask import Flask, render_template
import sqlite3

# Setting up Flask
app = Flask(__name__)


# Create Flask Routes
@app.route("/")
def home():
    conn = sqlite3.connect('reddit_sentiment.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM ticker_sentiment")
    rows = cur.fetchall()
    return render_template("index.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
