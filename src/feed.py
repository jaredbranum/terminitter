# feed module for terminitter

class Feed:
  def __init__(self, twitter):
    self.twitter = twitter
    self.connected = True
  
  def is_connected(self):
    return self.connected #TODO: self.connected
  
  def newest_tweets(self):
    newest = self.twitter.GetHomeTimeline()
    self.connected = False
    return newest
    