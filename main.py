from sys import argv
from time import sleep
from os import getenv
from dotenv import load_dotenv
from supabase import Client, create_client

from twitter import TwitterScarper
from tlgrm import TelegramParser


def main(screen_name, limit, supabase, twitter_scraper, telegram_parser):

    # Get the account Twitter ID, and put a limit for the tweets
    account_id = twitter_scraper.get_twitter_id(screen_name)

    # Read the old tweets list
    old_tweets = supabase.table('tweets').select('tweet_id').execute().data
    old_tweets = [item['tweet_id'] for item in old_tweets]
    new_tweets = []

    # Retrieve the tweets
    print('Getting Tweets...')
    tweets = twitter_scraper.get_tweets(account_id, limit)

    # Push the tweets to The Telegram channel
    print('Pushing Tweets...')
    for tweet in tweets[::-1]:

        # Check if the code has already being passed
        # if so, don't passed a second time
        if str(tweet.id) not in old_tweets:
            print(' Pushing Tweet: {}'.format(tweet.id), end = "\r")
            new_tweets.append({'twitter_id': str(account_id), 'tweet_id': str(tweet.id)})
            # telegram_parser.send_message(tweet.text)

            # The sleep is omportant, because when sending
            # to many parse requests without sleep, it breaks
            sleep(3)

    if len(new_tweets) != 0:
        # Save the new list of already parsed tweets
        supabase.table('tweets').insert(new_tweets).execute()


if __name__ == '__main__':
    # Parse the arguments list
    if len(argv) < 3:
        print('Must provide 2 arguments')
        exit()
    if len(argv) > 3:
        print('Must provide 2 arguments only')
        exit()

    screen_name = argv[1]
    limit = int(argv[2])

    # Load the Credentials & API Keys
    load_dotenv()
    BEARER_TOKEN = getenv('BEARER_TOKEN')
    BOT_TOKEN = getenv('BOT_TOKEN')
    CHAT_ID = getenv('CHAT_ID')
    DATA_DIR = getenv('DATA_DIR')
    SUPABASE_URL = getenv("SUPABASE_URL")
    SUPABASE_KEY = getenv("SUPABASE_KEY")

    # Create Supabase connection
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Create Scraper, telegram_parser objects
    twitter_scraper = TwitterScarper(BEARER_TOKEN)
    telegram_parser = TelegramParser(BOT_TOKEN, CHAT_ID)

    # Call the function
    main(screen_name, limit, supabase, twitter_scraper, telegram_parser)
