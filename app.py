# Dependencies
import praw
import pandas as pd
from config import client_id, client_secret, user_agent
from tickers import Ticker, scrape_tickers, scrape_IPOs, remove_duplicates, query_list, recent_IPO_list, upcoming_IPO_list

# Scrape to get updated tickers and company names for stocks and ETFs
scrape_tickers()

queries = []

# Build raw query list with ticker abbrevation and name of company
for query in query_list:
    ticker = "$" + query.abbrev
    queries.append(ticker)
    queries.append(query.abbrev)
    queries.append(query.name)

# Create connection to Reddit application
reddit = praw.Reddit(client_id=client_id,      # your client id
                     client_secret=client_secret,  # your client secret
                     user_agent=user_agent,  # user agent name
                     username="",     # your reddit username
                     password="")     # your reddit password

submissions_list = []
comments_list = []

subreddit_list = ['Stocks']

# Loop through list of Subreddits
for subreddit in subreddit_list:
    subreddit = reddit.subreddit(subreddit)
    # Loop through query list to query subreddit with each keyword
    for q in queries[:500]:  # slice to first 500 queries for testing purposes
        # Loop through submission results from keyword query
        # Change time filter as needed - set to hour for testing purposes
        for submission in subreddit.search(q, sort="top", time_filter="hour"):
            submission_obj = {
                "Post_Type": "Submission",
                "Submission_ID": submission.id,
                "Title": submission.title,
                "Author": submission.author,
                "Body": submission.selftext,
                "Distinguished": submission.distinguished,
                "Num_Comments": submission.num_comments,
                "Name": submission.name,
                "Permalink": submission.permalink,
                "URL": submission.url,
                "Score": submission.score,
                "Upvote_Ratio": submission.upvote_ratio,
                "Created_Date_UTC": [submission.created_utc]
            }
            print(submission_obj)
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
                    "Parent_Comment_ID": comment.parent_id,
                    "Author": comment.author,
                    "Body": [comment.body],
                    "Distinguished": comment.distinguished,
                    "Is_Author": comment.is_submitter,
                    "Permalink": comment.permalink,
                    "Score": comment.score,
                    "Created_Date_UTC": [comment.created_utc]
                }
                print(comment_obj)
                comments_list.append(comment_obj)

# print(submissions_list)
# print(comments_list)
