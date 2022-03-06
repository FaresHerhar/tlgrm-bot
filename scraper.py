from typing import List
import requests
import tweepy

from config import CDN_API_ID, CDN_API_NAME, BOT_TOKEN, CHAT_ID, TLGRM_TEXT


def telegram_bot_send_text(bot_message: str):
    response = requests.get(TLGRM_TEXT.format(BOT_TOKEN, CHAT_ID, bot_message))
    return response.json()


class Scarper:
    """ Twitter scraper class.
    
    A class containg methods that allows us to fetch basic data about tweets
    using the Twitter API V2, and some twitter end points.

    Attributes:
        _client: A protectd tweepy.Client object that permits us to access the API.
    """

    def __init__(self, BEARER_TOKEN: str) -> None:
        """Constructor.
        
        Intitiate a tweepy client using the Bearer Token.
        """
        # Authenticate
        self._client = tweepy.Client(BEARER_TOKEN, wait_on_rate_limit=True)


    def get_tweets(self, account_id: str, limit: int) -> List[tweepy.tweet.Tweet]:
        """ Fetches tweets of a user.

        Retrieves a specific number of tweets for a specific user.

        Args:
        account_id (str):
            The twitter account id.
        limit (int):
            The number of tweets to retrieve.
        
        Returns:
            A list of tweet.Tweet objects, in which each object contains all data.
        """
        tweets = []

        # Get the tweets using the pagination option
        # so i can control the number of tweets scraped.
        for tweet in tweepy.Paginator(self._client.get_users_tweets, id=account_id,
                                        tweet_fields=['text'],
                                        max_results=100).flatten(limit=limit):
            
            # Making sure that I am, taking tweets only, without any retweets.
            # After chacking the tweets checks, the tweets starts with 'RT '
            if not tweet.text.startswith('RT '):
                tweets.append(tweet)

        return tweets


    @staticmethod
    def get_twitter_id(screen_name: str) -> str:
        """ A static method to fetch Twitter account ID.

        Retrieves a twitter account ID from the account username.

        Args:
        screen_name (str):
            The twitter account username
        
        Returns:
            A string that represents the twitter account ID.
        """
        # Get the output as a json data
        # After that you'll get a dictionary into a single element list
        json_data = requests.get(CDN_API_ID.format(screen_name)).json()
        return json_data[0]['id']


    @staticmethod
    def get_twitter_screen_name(account_id: str) -> str:
        """ A static method to fetch Twitter account username.

        Retrieves a twitter account username from the account ID.

        Args:
        account_id (str):
            The twitter account ID
        
        Returns:
            A string that represents the twitter account username.
        """
        # Get the output as a json data
        # After that you'll get a dictionary into a single element list
        json_data = requests.get(CDN_API_NAME.format(account_id)).json()
        return json_data[0]['screen_name']


if __name__ == '__main__':
    print(Scarper.get_twitter_id('elonmusk'))
    print(Scarper.get_twitter_screen_name('44196397'))
