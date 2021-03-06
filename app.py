# Dependencies
import praw
import pandas as pd
from config import client_id, client_secret, user_agent
from tickers import Ticker, scrape_tickers, query_list

# Scrape to get updated tickers and company names
scrape_tickers()

queries = []

for query in query_list:
    queries.append(query.abbrev)
    queries.append(query.name)

reddit = praw.Reddit(client_id=client_id,      # your client id
                     client_secret=client_secret,  # your client secret
                     user_agent=user_agent,  # user agent name
                     username="",     # your reddit username
                     password="")     # your reddit password


subreddit_list = ['Stocks']

for subreddit in subreddit_list:
    subreddit = reddit.subreddit(subreddit)
    # for submission in subreddit.hot(limit=10):
    #    print(submission.title)
    for q in queries[:10]:
        for submission in subreddit.search(q, sort="top", limit=10):
            print(submission.title)
            print(submission.author)
            print(submission.created_utc)
