from tweepy import Stream
from tweepy.streaming import StreamListener
import auth
import json

text = "Shopwecan.com"

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')

class listener(StreamListener):

    def on_data(self, data):
        
        all_data = json.loads(data)
        id_tweet = all_data['id_str']
        tweet = all_data['text']
        username = all_data['user']['screen_name']
        
        if not contains_word(tweet, 'shopwecan.com') and not contains_word(tweet, 'Shop we can'):
            print(username, tweet)
            api.update_status(
                status='@' + username + ' ' + text,
                in_reply_to_status_id=id_tweet,
                wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True
            )

        return True

    def on_error(self, status):
        print(status)
        
api, auth = auth.auth()
        
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Air-pods", "wireless headset", "wireless headset bluetooth", "replica air-pods original size", "shop wireless headset bluetooth", "replica shop", "shopwecan"])

time.sleep(90)#Tweet every 15 minutes
