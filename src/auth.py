# auth module for terminitter

from oauth2 import * 
from oauthtwitter import OAuthApi
import os
import sys

def get_app_keys():
  if os.path.isfile('../terminitter.keys'):
    keyfile = open('../terminitter.keys', 'r')
    terminitter_keys = keyfile.read().splitlines()
    keyfile.close()
    return [terminitter_keys[0], terminitter_keys[1]]
  else:
    print('No terminitter.keys file found.')
    sys.exit(1)

def get_user_tokens(app_key, app_secret_key):
  if not os.path.isfile('../terminitter.oauth'): # no user tokens found, create some
    twitter = OAuthApi(app_key, app_secret_key)
    temp_credentials = twitter.getRequestToken()

    print(twitter.getAuthorizationURL(temp_credentials))
    oauth_verifier = raw_input('Go the the URL above, and paste the PIN here: ')
    tokens = twitter.getAccessToken(temp_credentials, oauth_verifier)

    oauthf = open('../terminitter.oauth', 'w')
    oauthf.write(tokens['oauth_token'] + '\n' + tokens['oauth_token_secret'])
    oauthf.close()
    return [access_token['oauth_token'], access_token['oauth_token_secret']]
  else: # read user tokens from file
    oauthf = open('../terminitter.oauth', 'r')
    oauth_tokens = oauthf.read().splitlines()
    return [oauth_tokens[0], oauth_tokens[1]]
    
def login():
  app_keys = get_app_keys()
  user_tokens = get_user_tokens(*app_keys)
  return OAuthApi(*(app_keys + user_tokens))

