import tweepy


auth = tweepy.OAuth1UserHandler(
   "xJm28uTOoZtTJDj87cKLfaAyP", "YSada81K5gHP9lAFD1ozwrxfSZ5OUllv2eW6OzGh0WBNWevpkg", "1374320677902151687-DdnIbRTzK54noRh33gm4PBKECwuN6D", "3Eg7JRwDIwi8IQUskGZJ97PUZw15Oq9Ozz1AFSpyUzWdx"
)

api = tweepy.API(auth) #api connecting to the auth

public_tweets = api.home_timeline() #all the tweets in ur timeline
for tweet in public_tweets:
    print(tweet.text)