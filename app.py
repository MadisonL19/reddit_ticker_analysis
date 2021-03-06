import praw
import pandas as pandas
from config import client_id, client_secret, user_agent


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
