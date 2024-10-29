# twitter_search.py

import tweepy
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET,
    TWITTER_BEARER_TOKEN
)

# Initialize Tweepy client with OAuth 1.0a User Context
client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

def search_adpod_tweets(query="#AdPod OR #Advertising OR #Marketing", max_results=10):
    try:
        tweets = client.search_recent_tweets(
            query=query,
            tweet_fields=['author_id'],
            max_results=max_results
        )
        if not tweets.data:
            return []
        tweet_links = [
            (tweet.text, f"https://twitter.com/{tweet.author_id}/status/{tweet.id}")
            for tweet in tweets.data
        ]
        return tweet_links
    except tweepy.TweepyException as e:
        print(f"Error searching tweets: {e}")
        return []

def post_tweet_comment(tweet_url, comment_text):
    tweet_id = tweet_url.split("/")[-1]
    try:
        response = client.create_tweet(text=comment_text, in_reply_to_tweet_id=tweet_id)
        print(f"Comment posted successfully: {response}")
        return comment_text
    except tweepy.TweepyException as e:
        print(f"Error posting comment: {e}")
        return f"Error posting comment: {e}"
