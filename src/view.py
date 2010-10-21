# view module for terminitter

from datetime import datetime
import time

TWEET_COLOR = '\033[0m'
USERNAME_COLOR = '\033[38;5;39m' # TODO: change to twitter logo color (or close)
AT_SIGN_COLOR = '\033[1;37m'
TIME_COLOR = '\033[0;37m'
NO_COLOR = '\033[0m'
# TODO: probably switch to use fabulous for colored text

def print_tweet(tweet):
  user = tweet['user']['screen_name']
  text = tweet['text']
  ttime = format_tweet_time(tweet['created_at'])
  #import pdb; pdb.set_trace()
  if True: # 256 colors
    print '['+TIME_COLOR+ttime+NO_COLOR+'] '+AT_SIGN_COLOR+'@'+NO_COLOR+USERNAME_COLOR+user+NO_COLOR+' > '+TWEET_COLOR+text+NO_COLOR
  else: # TODO: 16 colors
    print 'whatever'
    
def format_tweet_time(tweettime):
  dtime = time.strptime(tweettime, "%a %b %d %H:%M:%S +0000 %Y")
  hr = dtime.tm_hour % 12
  if hr == 0:
    hr = '12'
  elif hr < 10:
    hr = '0' + str(hr)
  else:
    hr = str(hr)
  
  # TODO: same for minutes
    
  return hr + ':' + mn
  
  #ttime = str(dtime.tm_hour % 12) + ":" + str(dtime.tm_min)
  