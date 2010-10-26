# growl module for terminitter

from urllib2 import urlopen
from os import path, makedirs
import Growl

class Growler:
  
  def __init__(self):
    self.g = Growl.GrowlNotifier('terminitter', ['tweet'])
    self.g.register()
  
  def _get_image(self, username, url): # TODO: some sort of caching
    img_folder = path.join(path.dirname(path.realpath(__file__)),'../images')
    if not path.exists(img_folder):
      makedirs(img_folder)
    img_path = path.join(img_folder, username)
    f = open(img_path, 'wb')
    f.write(urlopen(url).read())
    f.close()
    return Growl.Image.imageFromPath(img_path)
  
  def alert(self, tweet):
    #import pdb; pdb.set_trace()
    user = tweet['user']['screen_name']
    text = tweet['text']
    image = self._get_image(user, tweet['user']['profile_image_url'])
    self.g.notify('tweet', user, text, icon=image)