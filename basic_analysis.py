import os
import re
import json 


locations = [places for places in os.listdir("data")]
#print(locations)

key_accounts = []

tweets_count = 0
user_attributes = ["id","screen_name","followers_count","friends_count","time_zone","geo_enabled","geo","coordinates"]

user_data = dict()

hash_counts = dict()
for i in locations:

	if i != ".DS_Store":
 		with open("data/"+str(i)) as json_data:
			print("data/",i)
			data = json.load(json_data, strict=False)
	# 		for tweet in data['statuses']:
 #                if tweet['user']['id'] not in user_data.keys:
 #                    user_data[tweet['user']['id']]={"screen_name": tweet['user']['screen_name'],"followers_count": tweet['user']['followers_count'],"friends_count": tweet['user']['friends_count'],"time_zone": tweet['user']['time_zone'],"geo_enabled": tweet['user']['geo_enabled'],"geo": tweet['user']['geo'],"coordinates": tweet['user']['coordinates']}
                    
	# 			if(tweet['user']['followers_count'] > 300 ):
	# 				if(tweet['user']['screen_name'] not in key_accounts):
	# 					key_accounts.append(tweet['user']['screen_name']);
                
#                 tweets_count = tweets_count+1


				# print(tweet)
				# x = x+1
				# if(x==1):
					# break
		continue

