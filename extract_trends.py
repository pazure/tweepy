import tweepy 



CONSUMER_KEY = 'A7VXArZ0vCW2o5zpxBct3Mm6R'
CONSUMER_SECRET = 'SLZ9PcqzWAdixoKKwyT1VJoeHqiNz0uaXaoieTbxvKYouZ3uYA'
ACCESS_KEY = '1270144792815636487-1LZF0AEeRM88hfUKDCDhyzjHlJEKyy'
ACCESS_SECRET = '9GPgKScJOXzJ05CoNAj5GbIJfH0vuggaLhU4yIzL7etQc'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# trends = api.trends_available()

trends_gh = api.trends_place(23424824)

t0 = trends_gh[0]
TRENDS = t0['trends']
trends_box = []

for TREND in TRENDS:
	trends_box.append(TREND['name'])
    
top5 = trends_box[:50]
trendsName = ' '.join(top5)
print(trendsName)