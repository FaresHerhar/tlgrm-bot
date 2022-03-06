from scraper import Scarper
from config import BEARER_TOKEN

# Create Scraper object
scraper = Scarper(BEARER_TOKEN)

screen_name = 'wikileaks'
account_id = scraper.get_twitter_id(screen_name)
limit = 10

tweets = scraper.get_tweets(account_id, limit)

for tweet in tweets:
    print(tweet.id, tweet.text)
    print('-----\n')
