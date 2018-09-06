#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 12:45:09 2018

@author: aayushsharma
"""
import auth
import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import matplotlib.pyplot as plt
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#user = api.get_user('twitter')
#print(user.screen_name)
#print(user.followers_count)

query=input("Enter your query: ")
#Get tweets using tweepy 
max_tweets = 10
tweets = [status for status in tweepy.Cursor(api.search,
                                             q=query,
                                             result_type="recent",
                                             tweet_mode="extended",
                                             lang="en",
                                             ).items(max_tweets)]
#parse tweet texts
#print(tweets)
def tweet_sent(x):
    analyzer = SIA()
    score =analyzer.polarity_scores(x)
    return(score)
    
tweet_text=[]
tweet_date=[]
tweet_score=[]
for tweet in tweets:
    tweet = tweet._json
    if 'retweeted_status' in tweet:
        tweet_text.append(tweet['retweeted_status']['full_text'])
        tweet_date.append(tweet['created_at'])
        tweet_score.append(tweet_sent(tweet['retweeted_status']['full_text']))
    else:
        tweet_text.append(tweet['full_text'])
        tweet_date.append(tweet['created_at'])
        tweet_score.append(tweet_sent(tweet['full_text']))

tweet_data = list(zip(tweet_text,tweet_date,tweet_score))
print(tweet_data)
