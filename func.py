import requests

from config import TWITTER_CDN_API

def get_twitter_id(screen_name):
    # Get the output as a json data
    # After that you'll get a dictionary into a single element list
    json_data = requests.get(TWITTER_CDN_API.format(screen_name)).json()[0]
    return json_data['id']

if __name__ == '__main__':
    print(get_twitter_id('elonmusk'))
