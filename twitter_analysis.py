import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Euro 2024')\
                    .setSince("2024-01-01")\
                    .setUntil("2024-05-15")\
                    .setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in text_tweets]
    print(text_tweets)

get_tweets()