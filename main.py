if __name__ == '__main__':
    # import sys.argv as argv
    from sys import argv
    from time import sleep
    from os import listdir

    from func import save_object, load_object
    from scraper import TwitterScarper
    from parser import TelegramParser
    from config import (TWT_BEARER_TOKEN, TLGRM_BOT_TOKEN,
                        TLGRM_CHAT_ID, DATA_DIR)


    # Parse the arguments list
    if len(argv) < 3:
        print('Must provide 2 arguments')
        exit()
    if len(argv) > 3:
        print('Must provide 2 arguments only')
        exit()

    screen_name = argv[1]
    limit = int(argv[2])

    # Check if the file already exists
    if '{}.pickle'.format(screen_name) not in listdir(DATA_DIR):
        save_object('{}/{}.pickle'.format(DATA_DIR, screen_name), [])

    # Create Scraper, Parser objects
    scraper = TwitterScarper(TWT_BEARER_TOKEN)
    parser = TelegramParser(TLGRM_BOT_TOKEN, TLGRM_CHAT_ID)

    # Get the account Twitter ID, and put a limit for the tweets
    account_id = scraper.get_twitter_id(screen_name)

    # Read the old tweets list
    old_tweets = load_object('{}/{}.pickle'.format(DATA_DIR, screen_name))
    new_tweets = []

    # Retrieve the tweets
    tweets = scraper.get_tweets(account_id, limit)

    # Push the tweets to The Telegram channel
    for tweet in tweets[::-1]:
        # Check if the code has already being passed
        # if so, don't passed a second time
        if tweet.id not in old_tweets:
            new_tweets.append(tweet.id)
            parser.send_message(tweet.text)

            # The sleep is omportant, because when sending
            # to many parse requests without sleep, it breaks
            sleep(2)

    # Save the new list of already parsed tweets
    save_object('{}/{}.pickle'.format(DATA_DIR, screen_name),
                old_tweets + new_tweets)
