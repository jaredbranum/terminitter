# feed module for terminitter

class Feed:
  MAX_TWEETS = 50

  def __init__(self, twitter):
    self.twitter = twitter
    self.connected = True
    self.last_tweet_id = 1
  
  def is_connected(self):
    return self.connected #TODO: self.connected
  
  def newest_tweets(self):
    tweets = self.twitter.GetHomeTimeline(
      {'since_id': self.last_tweet_id, 'count': Feed.MAX_TWEETS}
    )
    if tweets:
      self.last_tweet_id = tweets[0]['id']
    return tweets

