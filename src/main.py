# terminitter v0.1
# TODO: license and crap

from auth import login
from feed import Feed
from threading import Thread
from sys import argv, exit
from getopt import getopt, GetoptError

def main(argv):
  try:
    opts, args = getopt(argv, "chg", ["256color", "help", "growl"])
  except GetoptError:
    usage()
    exit(2)
  
  c = False
  g = False
  for opt, arg in opts:
      if opt in ("-c", "--256color"):
        c = True
      elif opt in ("-h", "--help"):
        usage()
        exit()
      elif opt in ("-g", "--growl"):
        g = True
        
  options = {'256color': c, 'growl': g}
  
  twitter = login()
  timeline = Feed(twitter, options)
  
  poll_thread = Thread(target=timeline.poll)
  poll_thread.daemon = True
  poll_thread.start()
  
  while True: # TODO: things to do while the program is running
    pass

def usage():
  print 'wrong' # TODO: write this garbage
  
if __name__ == "__main__": #TODO: command line args (growl, disable 256 color, etc)
    main(argv[1:])
