from typing import List
import tweepy

class TwitterScarper:
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
            
            tweets.append(tweet)

        return tweets


    def get_twitter_id(self, screen_name: str) -> str:
        """ A static method to fetch Twitter account ID.

        Retrieves a twitter account ID from the account username.

        Args:
        screen_name (str):
            The twitter account username
        
        Returns:
            A string that represents the twitter account ID.
        """
        # Get the output as a response object, After that you'll get a dictionary
        # Response(data=<User id=16589206 name=WikiLeaks username=wikileaks>, includes={}, errors=[], meta={})
        return self._client.get_user(username=screen_name)[0]['id']


    def get_twitter_username(self, account_id: str) -> str:
        """ A static method to fetch Twitter account username.

        Retrieves a twitter account username from the account ID.

        Args:
        account_id (str):
            The twitter account ID
        
        Returns:
            A string that represents the twitter account username.
        """
        # Get the output as a response object, After that you'll get a dictionary
        # Response(data=<User id=16589206 name=WikiLeaks username=wikileaks>, includes={}, errors=[], meta={})
        return self._client.get_user(username=account_id)[0]['username']
