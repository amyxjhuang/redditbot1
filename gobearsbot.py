#!/usr/bin/python
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent='yay')
subreddit = reddit.subreddit('school')

keyphrases = ['uc berkeley','cal','berkeley','go bears','Go bears']

for comment in subreddit.comments(limit=25):
    time.sleep(2)
    if comment.body in keyphrases:
        comment.reply("GO BEARS!")
        print ("replied to comment" + comment.id)
