# terminitter v0.1
# TODO: license and crap

from auth import login
from feed import Feed
from threading import Thread

def main():
  twitter = login()
  timeline = Feed(twitter)
  poll_thread = Thread(target=timeline.poll)
  poll_thread.daemon = True
  poll_thread.start()
  
  while True: # TODO: things to do while the program is running
    pass
  
if __name__ == "__main__": #TODO: command line args (growl, disable 256 color, etc)
    main()
  