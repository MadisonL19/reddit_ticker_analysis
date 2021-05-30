# WIP - REDDIT STOCK SENTIMENT ANALYZER

## Business Case

Reddit is a popular social media platform that many investors utilize to discover and discuss different stocks. As more retail investors join the stock market, the discussions that take place on Reddit have an increasingly signficant impact on the movement of particular stocks.

What if we could analyze submissions and comments from popular subreddit forums to identify potential trends before they occur? Furthermore, can we effectively define a correlation or pattern between the majority sentiment and price action for the day? These two questions are actively being explored by not only the community, but also institutions and hedge funds, as everyone continues to strive to seek _alpha_.

By using sentiment analysis on Reddit submissions and their corresponding comments, I created a model to classify whether investors are bullish, bearish, or neutral on a given stock. Frequency of mentions and daily price change are also provided to highlight the discovery; as frequency can point to momentum, while price change can support accuracy of findings. 

The model is integrated into a Flask application which uses a SQLite database to store historical findings. The JavaScript Plotly library is used to visualize the results.

#### Skills used - Machine Learning with NLP, Web-Scraping, Full-Stack Development with Flask and SQLite, Data Analysis
#### Technologies used - Python, JavaScript, Pandas, NLTK, Flask, SQLite, Plotly
