import tweepy

from config import BEARER_TOKEN

# The account that we're meant to get its data
# screen_name = 'wikileaks'
account_id = '16589206'
tweets = []

# Authenticate
client = tweepy.Client(BEARER_TOKEN)

# Get the tweets
for tweet in tweepy.Paginator(client.get_users_tweets, id=account_id,
                                tweet_fields=['text'],
                                max_results=100).flatten(limit=10):
    
    tweets.append(tweet)

print(len(tweets))
