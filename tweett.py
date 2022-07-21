import tweepy

ckey = "tkKT07OE4g0Suv4YVSljxJGf7"
csecret = "qtyPTFH0kIxtwXuEU6J9IXG0zP7Sd7mppldFGhGiLMjkbZ8cx6"
atoken = "4667182272-k8oByokAqVV9VTELbyIBlvIROzCm11aU7YWv6ol"
asecret = "eRYMGXSeHZkqvlfjWLd5ntx4GGvdFKjlTlXDVabYbcWCO"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

cricTweet = tweepy.Cursor(api.search, q='#ChaddiNahiSochBadlo').items(6000)
count=0
for tweet in cricTweet:
   print tweet.created_at, tweet.text, tweet.lang
   count=count+1
print count
