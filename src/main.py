# terminitter v0.1
# TODO: license and crap

from auth import login
from feed import Feed
from view import print_tweet

def main():
  twitter = login()
  timeline = Feed(twitter)

  while timeline.is_connected():
    for tweet in reversed(timeline.newest_tweets()):
      print_tweet(tweet)
  
if __name__ == "__main__":
    main()