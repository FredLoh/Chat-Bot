import json
import time
import os
from tweepy import API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


class DataStream(StreamListener):
    def __init__(self):
        super(DataStream, self).__init__()
        self.consumer_key = os.environ['HACKCU_APP_KEY']
        self.consumer_secret = os.environ['HACKCU_KEY_SECRET']
        self.oauth_key = os.environ['HACKCU_OAUTH_TOKEN']
        self.oauth_secret = os.environ['HACKCU_OAUTH_SECRET']
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.oauth_key, self.oauth_secret)
        self.api = API(self.auth)

    def get_home_timeline(self):
        tweet = self.api.user_timeline(id='709091333969870851', count=1, include_rts=True)
        status = tweet[0]
        json_string = json.dumps(status._json)
        json_string = json.loads(json_string)
        print json_string["text"]
        return json_string["text"]
