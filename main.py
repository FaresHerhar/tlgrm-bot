if __name__ == '__main__':
    from time import sleep
    from os import listdir

    from func import save_object, load_object
    from scraper import TwitterScarper
    from parser import TelegramParser
    from config import (TWT_BEARER_TOKEN, TLGRM_BOT_TOKEN,
                        TLGRM_CHAT_ID, DATA_DIR, DATA_FILE)

    # Check if the file already exists
    if 'tweets.pickle' not in listdir(DATA_DIR):
        save_object(DATA_FILE, [])

    # Create Scraper, Parser objects
    scraper = TwitterScarper(TWT_BEARER_TOKEN)
    parser = TelegramParser(TLGRM_BOT_TOKEN, TLGRM_CHAT_ID)

    # Read the old tweets list
    old_tweets = load_object(DATA_FILE)
    new_tweets = []

    # Get the account Twitter ID, and put a limit for the tweets
    screen_name = 'wikileaks'
    account_id = scraper.get_twitter_id(screen_name)
    limit = 4

    # Retrieve the tweets
    tweets = scraper.get_tweets(account_id, limit)

    # Push the tweets to The Telegram channel
    for tweet in tweets[::-1]:
        # Check if the code has already being passed
        # if so, don't passed a second time
        if tweet.id not in old_tweets:
            new_tweets.append(tweet.id)
            parser.send_message(tweet.text)
            sleep(3)

    # Save the new list of already parsed tweets
    save_object(DATA_FILE, old_tweets + new_tweets)
