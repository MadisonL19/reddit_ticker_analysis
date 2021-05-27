# Dependencies
from flask import Flask, render_template
from flask import jsonify
import json
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
    for row in rows[:1]:
        for item in row:
            print(item)
            # ticker symbol
            # date
            # count
            # sentiment
            # price change
    return render_template("index.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
