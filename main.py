if __name__ == '__main__':
    from time import sleep

    from scraper import TwitterScarper
    from parser import TelegramParser
    from config import TWT_BEARER_TOKEN, TLGRM_BOT_TOKEN, TLGRM_CHAT_ID

    # Create Scraper, Parser objects
    scraper = TwitterScarper(TWT_BEARER_TOKEN)
    parser = TelegramParser(TLGRM_BOT_TOKEN, TLGRM_CHAT_ID)

    # Get the account Twitter ID, and put a limit for the tweets
    screen_name = 'wikileaks'
    account_id = scraper.get_twitter_id(screen_name)
    limit = 10

    # Retrieve the tweets
    tweets = scraper.get_tweets(account_id, limit)

    # Push the tweets to Tlegram channel
    for tweet in tweets:
        parser.send_message(tweet.text)
        sleep(5)
