import tweepy 
import json

#Twitter API credentials

consumer_key = "UDcWtz23Pqj8fZ2ynPoP0rvNl"
consumer_secret = "Ms9hyFReK13kHcpcbGYknkZZCUEVUWSfFadGzR9j9ncodbueHn"
access_key = "2456487102-r2SpnynWDvvRrbtQ42K45qKBbcDrvQiBS0kTX9C"
access_secret = "wqWWy50LOhTZsf9ayYxDarI8Kf8nbwgUDBTto5NA9vsEF"   


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	alltweets=[]

	file_name = "profiles/"+screen_name
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, parser=tweepy.parsers.JSONParser())
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name, tweet_mode = "extended", count=200)
	alltweets.extend(new_tweets)
	#print(alltweets)
	#save the id of the oldest tweet less one
	oldest = alltweets[-1]['id'] - 1

	#save most recent tweets
	with open(file_name+"/"+str(oldest)+".json", "w+") as fp:
		json.dump(new_tweets,fp)
		# print(oldest)
		# print("\n")
	
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		# print("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name, tweet_mode = "extended", count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1]['id'] - 1

		#save most recent tweets
		with open(file_name+"/"+str(oldest)+".json", "w+") as fp:
			json.dump(new_tweets,fp)
			# print(oldest)
			# print("\n")
		
		# print("...%s tweets downloaded so far" % (len(alltweets)))


# get_all_tweets("chileaspheng")

get_all_tweets("xnshxl")


