import os
import re
import json 

#count_retweets keeps a global count of the retweets we have scraped
#count_tweets is a global count of tweets 
#count_quoted is the number of quoted texts

count_retweets=0
count_tweets=0
count_quoted=0

locations = [places for places in os.listdir("data")]
#print(locations)

hash_counts= dict()
for i in locations:
	if i != ".DS_Store":
		with open("data/"+str(i)) as json_data:
			print("data/",i)
			data = json.load(json_data, strict=False)
		for tweet in data['statuses']:
			count_tweets+=1
			if(tweet['full_text'].startswith("RT @")): #is a reetweet
				#print(tweet['full_text'][0:5])
				count_retweets+=1
				if(tweet['is_quote_status']==True): #the retweet is a quote
					count_quoted+=1

print("count_retweets ",count_retweets)
print("count_tweets ",count_tweets)
print("count_quoted ",count_quoted)
