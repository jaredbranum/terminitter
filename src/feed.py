# feed module for terminitter

from view import print_tweet
from time import sleep

class Feed:
  MAX_TWEETS = 50

  def __init__(self, twitter, args):
    self.twitter = twitter
    self.connected = True
    self.last_tweet_id = 1
    self.growl_enabled = args['growl']
    self.color = args['256color']
    if self.growl_enabled:
      from growl import Growler
      self.growl = Growler()
  
  def is_connected(self):
    return self.connected # TODO: self.connected
  
  def newest_tweets(self):
    tweets = self.twitter.GetHomeTimeline(
      {'since_id': self.last_tweet_id, 'count': Feed.MAX_TWEETS}
    )
    if tweets:
      self.last_tweet_id = tweets[0]['id']
    return tweets

  def poll(self): # always run in a separate thread
    while self.is_connected():
      ltid = self.last_tweet_id
      for tweet in reversed(self.newest_tweets()):
        print_tweet(tweet, self.color)
        if self.growl_enabled:# && ltid != 1:
          self.growl.alert(tweet)
      sleep(30) # poll every 30 sec to stay under the API limit
    

