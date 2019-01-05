#!/usr/bin/python
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent='yay')

subreddit = reddit.subreddit("bayarea")

keyphrase = 'uc berkeley'

for comment in subreddit.stream.comments():
    if keyphrase == comment.body:
        comment.reply("GO BEARS!")
# for submission in subreddit.hot(limit=5):
#     print("Title: ", submission.title)
#     print("Text: ", submission.selftext)
#     print("Score: ", submission.score)
#     print("---------------------------------\n")
