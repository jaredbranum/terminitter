# terminitter v0.1
# TODO: license and crap

from oauth2 import * 
from oauthtwitter import OAuthApi
import pprint
import os
import sys

if os.path.isfile('../terminitter.keys'):
  keyfile = open('../terminitter.keys', 'r')
  terminitter_keys = keyfile.read().splitlines()
  terminitter_key, terminitter_secret = terminitter_keys[0], terminitter_keys[1]
  keyfile.close()
else:
  print('No terminitter.keys file found.')
  sys.exit(1)

if not os.path.isfile('../terminitter.oauth'):
  twitter = OAuthApi(terminitter_key, terminitter_secret)
  temp_credentials = twitter.getRequestToken()

  print(twitter.getAuthorizationURL(temp_credentials))
  oauth_verifier = raw_input('Go the the URL above, and paste the PIN here: ')
  access_token = twitter.getAccessToken(temp_credentials, oauth_verifier)

  oauthf = open('../terminitter.oauth', 'w')
  oauthf.write(access_token['oauth_token'] + '\n' + access_token['oauth_token_secret'])
  oauthf.close()
  oauth_token, oauth_token_secret = access_token['oauth_token'], access_token['oauth_token_secret']
else:
  oauthf = open('../terminitter.oauth', 'r')
  oauth_tokens = oauthf.read().splitlines()
  oauth_token, oauth_token_secret = oauth_tokens[0], oauth_tokens[1]

# Do a test API call using our new credentials
twitter = OAuthApi(terminitter_key, terminitter_secret, oauth_token, oauth_token_secret)
user_timeline = twitter.GetUserTimeline()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(user_timeline)

