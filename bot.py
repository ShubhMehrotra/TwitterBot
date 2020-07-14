import tweepy
import time
CONSUMER_KEY='Placed Your Cosnumer  Key Here'
CONSUMER_SECRET='Placed Your Cosnumer Secret Key Here'
ACCESS_KEY='Placed Your Access Key Here'
ACCESS_SECRET='Placed Your Access Secret Key Here'


auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

test_list=[Placed your frineds twitter id here (Integer Value ) seperated by comma 
Note:Twitter id is different from username







]

for test in test_list:
        api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
        tweet_list = api.user_timeline(test )#To get tweets of particular user we’ll use:
        try:
            for tweet in tweet_list:
                print(api.retweet(tweet.id))
                print(api.create_favorite(tweet.id))
                time.sleep(40)
        except :
            pass
