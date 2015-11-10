from alchemyapi import AlchemyAPI
from TwitterSearch import *
import plotly.plotly as py
from plotly.graph_objs import Scatter
count=0.0
alch=AlchemyAPI()
val=0
city=""
words=[""]
#lat,long must be a long type
latitude=37.7576793
longitude=-122.5076407
place_name="San Fransisco"
radius=100
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(words) 
    tso.set_language('en')
    tso.set_geocode(latitude,longitude,radius,imperial_metric=False)# let's define all words we would like to have a look for
     # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'vuMMiwDubszCWPFJ7qwT1QIur',
        consumer_secret = 'JCfjstASKGENmA2f3bhBjhiKUl1Cdqi6Z1ANnKlWJ3DJevcYcG',
        access_token = '223808804-GIFIQw9Sw7U8CmOnUC7virOpHrnbQWEWih2fni4z',
        access_token_secret = '0EnNQicRpE2buDXU9hseWshSPPRwaU875fVx1XVJ4aY78'
     )
    ff=open(place_name,"a")
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        val=val+1
    	print("\n")
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        
        try:
            ff.write(tweet['text']+"\n")
            res=alch.sentiment("text", tweet['text'])
            for aa in res:
                if 'docSentiment' not in aa:
                    continue
                for dest in res['docSentiment']:
                    if 'score' not in dest:
                        continue
                    sc=res["docSentiment"]["score"]
                    count=count+ float(sc)
                    print count
        except UnicodeEncodeError:
            pass
        if val>=20:
            break        
    ff.close()
    with open (place_name, "r") as myfile:
        data=myfile.read()
    res1=alch.sentiment("text",data)
    file2=open("final","a")
    file2.write(place_name+ ""+words+str(count)+" "+res1["docSentiment"]["type"]+"\n")

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

