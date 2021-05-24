# Dependencies
import praw
import pandas as pd
from config import client_id, client_secret, user_agent
from tickers import Ticker, scrape_tickers, query_list, recent_IPO_list, upcoming_IPO_list

# Scrape to get updated tickers and company names for stocks and ETFs
scrape_tickers()

import_lists = [query_list, recent_IPO_list, upcoming_IPO_list]

tickers = []

# Build raw query list with ticker abbrevation and name of company
for i in import_lists:
    for item in i:
        if item.abbrev == 'A':
            item.abbrev = '-'
        tickers.append(item)

# Create connection to Reddit application
reddit = praw.Reddit(client_id=client_id,      # client id
                     client_secret=client_secret,  # client secret
                     user_agent=user_agent,  # user agent name
                     username="",     # your reddit username
                     password="")     # your reddit password

submissions_list = []
comments_list = []

subreddit_list = ['Stocks']

# Loop through list of Subreddits
for subreddit in subreddit_list:
    subreddit = reddit.subreddit(subreddit)
    # Loop through top posts from subreddit within specified timeframe
    for submission in subreddit.top(limit=None, time_filter="day"):
        submission_obj = {
            "Post_Type": "Submission",
            "Submission_ID": submission.id,
            "Title": submission.title,
            "Author": submission.author,
            "Body": submission.selftext,
            "Flair": submission.link_flair_text,
            "Distinguished": submission.distinguished,
            "Num_Comments": submission.num_comments,
            "Post_ID": submission.name,
            "URL": submission.url,
            "Score": submission.score,
            "Upvote_Ratio": submission.upvote_ratio,
            "Created_Date_UTC": [submission.created_utc]
        }
        submissions_list.append(submission_obj)
        submission.comments.replace_more(limit=0)
        submission.comments_sort = "top"
        # Limit number of comments return during testing
        submission.comment_limit = 100
        comments = submission.comments.list()
        # Loop through commments on each submission
        for comment in comments:
            comment_obj = {
                "Post_Type": "Comment",
                "Submission_ID": submission.id,
                "Comment_ID": comment.id,
                "Parent_ID": comment.parent_id,
                "Author": comment.author,
                "Body": [comment.body],
                "Flair": comment.author_flair_text,
                "Distinguished": comment.distinguished,
                "Is_Author": comment.is_submitter,
                "Score": comment.score,
                "Created_Date_UTC": [comment.created_utc]
            }
            comments_list.append(comment_obj)

# Convert lists of submissions and comments to pandas dataframe
submissions_df = pd.DataFrame(submissions_list)
comments_df = pd.DataFrame(comments_list)

#submissions_df.to_csv("submissions.csv", index=False)
#comments_df.to_csv("comments.csv", index=False)
