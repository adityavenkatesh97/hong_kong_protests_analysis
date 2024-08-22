import os
import re
import json 

locations = [places for places in os.listdir("data")]
#print(locations)

hash_counts= dict()
for i in locations:
	if(i!=".DS_Store"):
		with open("data/"+str(i)) as json_data:
			print("data/",i)
			data = json.load(json_data, strict=False)
		for tweet in data['statuses']:
			#print(tweet['full_text'])
			hashtags = re.findall(r"#(\w+)", tweet['full_text'])
			for k in hashtags:
				if k in hash_counts:
					hash_counts[k]+=1
				else:
					hash_counts[k]=1


print(hash_counts)
