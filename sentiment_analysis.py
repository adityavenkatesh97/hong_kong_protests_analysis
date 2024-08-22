from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
  
# function to print sentiments 
# of the sentence. 
def sentiment_scores(sentence): 
  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    #print("Overall sentiment dictionary is : ", sentiment_dict) 
    #print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    #print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    #print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    #print("Sentence Overall Rated As", end = " ") 
  
    # decide sentiment as positive, negative and neutral 
    #if sentiment_dict['compound'] >= 0.05 : 
    #    print("Positive") 
  
    #elif sentiment_dict['compound'] <= - 0.05 : 
    #   print("Negative") 
  
    #else : 
    #    print("Neutral") 
    return sentiment_dict['neg']
  
  
from datetime import datetime
import matplotlib.pyplot as plt
import os
import re
import json 

dates=[]
sent=[]
month = dict()
month = {"Jan":"1",
    "Feb":"2",
    "Mar":"3",
    "Apr":"4",
    "May":"5",
    "Jun":"6",
    "Jul":"7",
    "Aug":"8",
    "Sep":"9",
    "Oct":"10",
    "Nov":"11",
    "Dec":"12"}

locations = [places for places in os.listdir("data")]
#print(locations)

for i in locations:
    if i != ".DS_Store":
        with open("data/"+str(i)) as json_data:
            print("data/",i)
            data = json.load(json_data, strict=False)
        for tweet in data['statuses']:
            if(tweet['full_text'].startswith("RT @")): #is a reetweet, then the full text is stored whithin retweeted_status of the json
                text = tweet['retweeted_status']['full_text']
                wiki = sentiment_scores(tweet['retweeted_status']['full_text'])
            else:
                text = tweet['full_text']
                wiki = sentiment_scores(tweet['full_text'])
            #print(text," ---- ",wiki)
            mon = tweet['created_at'][4:7]
            day = tweet['created_at'][8:10]
            tweet_date = day+"/"+month[mon]+"/2019"
            print(tweet_date," -- ",wiki)
            print("\n")
            dates.append(tweet_date)
            sent.append(wiki)



date_objects = [datetime.strptime(date, '%d/%m/%Y').date() for date in dates]

plt.plot(sent,date_objects)
plt.show()
