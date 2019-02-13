import json
import urllib.request
import requests
import re

tweets = []                 
for line in open('small_data_ukge.json'):           # reading the lines in given json file
    try:
        tweets.append(json.loads(line))             # appending the dictionaries in json file to a the list tweets
    except:
        continue
#print(tweets)

for tweet in tweets:
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(tweet))     # finding all urls in 																each tweet present
                                                                                                                        #in the list tweets, 																and returning the 
                                                                                                                        #list of all urls in 																variable urls
    
    for url in urls:
        try:
            res = urllib.request.urlopen(url)       # getting the actual url (expanding url) and storing the address in actual_url
            actual_url = res.geturl()
            print(actual_url)
            tweet.update({"expanded_url": actual_url})	# updating each element tweet(which is a dictionary) in the list tweets with a new k,v 																		pair
            

        except:
            actual_url = url
            print(actual_url)
            tweet.update({"expanded_url": actual_url})
  
#print(tweets)

with open('data.json','w') as jf:           # storing the updated data as dictionaries in a new json file
    for tweet in tweets:
        json.dump(tweet,jf)
        jf.write('\n')
        








        




