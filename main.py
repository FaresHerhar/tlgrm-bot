from scraper import Scarper
from config import BEARER_TOKEN

# Create Scraper object
scraper = Scarper(BEARER_TOKEN)

screen_name = 'wikileaks'
account_id = scraper.get_twitter_id('16589206')
limit = 10


tweets = scraper.get_tweets(account_id, limit)
print(len(tweets))
