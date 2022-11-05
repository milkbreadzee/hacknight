"""
import random
import twt

#message - user inputted of type string, fn going to return string

"""

import tweepy

def get_response(message: str) -> str:
   # p_message = message.lower() # to make the input case frienly with python
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAABrkiwEAAAAABtWiaZzW831nTzLRIG7v5TuLRPo%3DIlQiW2IGdK7TWcd1qqm75rd1lLVdp7NnQsARkC0JoUSiSTtuGg')

    tweets = client.search_recent_tweets(message)

    return tweets.data[0]



"""
    if p_message == 'hello':
        return 'hewwowow'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
        #dice roll sim
    
    if p_message == 'help':
        return '`help msg`'

"""
    #return 'I dont understand what youre writing, try writing "hello" or "roll"'
