# view module for terminitter

from time import strptime, strftime
from datetime import datetime, timedelta
#from fabulous import fg256, bg256
# TODO: switch view to use curses

TWEET_COLOR = '\033[0m'
USERNAME_COLOR = '\033[38;5;39m' # TODO: change to twitter logo color (or close)
AT_SIGN_COLOR = '\033[1;37m'
TIME_COLOR = '\033[0;37m'
TIME_BRACKET_COLOR = '\033[1;30m'
SEPARATOR_COLOR = '\033[38;5;172m'
NO_COLOR = '\033[0m'

def print_tweet(tweet, full_color=False):
  user = tweet['user']['screen_name']
  text = tweet['text']
  ttime = format_tweet_time(tweet['created_at'])
  #import pdb; pdb.set_trace()
  if full_color: # 256 colors
    print (
      TIME_BRACKET_COLOR+'['+NO_COLOR+
      TIME_COLOR+ttime+NO_COLOR+
      TIME_BRACKET_COLOR+'] '+NO_COLOR+
      AT_SIGN_COLOR+'@'+NO_COLOR+
      USERNAME_COLOR+user+NO_COLOR+
      SEPARATOR_COLOR+' > '+NO_COLOR+
      TWEET_COLOR+text+NO_COLOR
    )
  else: # TODO: 16 colors
    print 'whatever'
    
def format_tweet_time(tweettime):
  # TODO: detect timezone and dst rather than hardcode to EST
  return (
    datetime.strptime(tweettime, "%a %b %d %H:%M:%S +0000 %Y")
    + timedelta(hours=8) # EST
  ).strftime("%I:%M")
