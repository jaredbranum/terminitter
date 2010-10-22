# growl module for terminitter

import Growl

class Growler:
  
  def __init__(self):
    self.g = Growl.GrowlNotifier('terminitter', ['status'])
    self.g.register()
  
  def alert(self, title, message):
    self.g.notify('status', title, message)