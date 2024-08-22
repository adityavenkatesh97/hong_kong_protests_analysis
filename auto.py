from get_user_tweets import get_all_tweets
import os



f= open("rem_user_accounts_2","r")


content = f.readlines()

num_accounts_done = 0

for i in content:
	num_accounts_done += 1
	try:
		os.mkdir("profiles2/"+i[:-1])
		get_all_tweets(i[:-1])
		print(num_accounts_done)
		print("Current account: " + i)
	except(Exception):
		print("profiles/"+i[:-1])
		continue
	
		# print(i[:-1])
		