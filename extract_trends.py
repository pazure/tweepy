import tweepy 



CONSUMER_KEY = 'your conumer key'
CONSUMER_SECRET = 'your consumer secret'
ACCESS_KEY = 'your access key'
ACCESS_SECRET = 'you access secret'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# trends = api.trends_available()

trends_gh = api.trends_place(WOEID)

t0 = trends_gh[0]
TRENDS = t0['trends']
trends_box = []

for TREND in TRENDS:
	trends_box.append(TREND['name'])
    
top5 = trends_box[:50]
trendsName = ' '.join(top5)
print(trendsName)
