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
    # conn = sqlite3.connect('reddit_sentiment.db')
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM ticker_sentiment")
    # rows = cur.fetchall()
    # data_arr = []
    # data_obj = {}
    # for row in rows:
    #     counter = 1
    #     for item in row:
    #         if counter == 1:
    #             data_obj["ticker"] = item
    #             counter += 1
    #         if counter == 2:
    #             data_obj["date"] = item
    #             counter += 1
    #         if counter == 3:
    #             data_obj["count"] = item
    #             counter += 1
    #         if counter == 4:
    #             data_obj["sentiment"] = item
    #             counter += 1
    #         else:
    #             data_obj["price_change"] = item
    #     data_arr.append(json.dumps(data_obj))
    # return render_template("index.html", rows=data_arr)
    return render_template("index.html")


@app.route("/data")
def get_data():
    conn = sqlite3.connect('reddit_sentiment.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM ticker_sentiment")
    rows = cur.fetchall()
    data_arr = []
    data_obj = {}
    for row in rows[:1]:
        counter = 1
        for item in row:
            if counter == 1:
                print(f"index: {item}")
                data_obj["index"] = item
            if counter == 2:
                print(f"ticker: {item}")
                data_obj["ticker"] = item
            if counter == 3:
                print(f"date: {item}")
                data_obj["date"] = item
            if counter == 4:
                print(f"count: {item}")
                data_obj["count"] = item
            if counter == 5:
                print(f"sentiment: {item}")
                data_obj["sentiment"] = item
            else:
                print(f"price_change: {item}")
                data_obj["price_change"] = item
            counter = counter + 1
        data_arr.append(data_obj)
    return jsonify(data_arr)


if __name__ == '__main__':
    app.run(debug=True)
