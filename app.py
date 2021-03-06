# Dependencies
import praw
import pandas as pandas
from config import client_id, client_secret, user_agent
from tickers import Ticker, scrape_tickers, query_list

# Scrape to get updated tickers and company names
scrape_tickers()

for query in query_list:
    print(query.abbrev)
    print(query.name)

reddit = praw.Reddit(client_id=client_id,      # your client id
                     client_secret=client_secret,  # your client secret
                     user_agent=user_agent,  # user agent name
                     username="",     # your reddit username
                     password="")     # your reddit password


subreddit_list = ['Stocks']

for subreddit in subreddit_list:
    subreddit = reddit.subreddit(subreddit)
    print(subreddit)
    for submission in subreddit.hot(limit=10):
        print(submission.title)
