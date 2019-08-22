import twitter
import json

with open("auth.json", "r") as authFile:
    auth = json.load(authFile)

api = twitter.Api(consumer_key=auth["consumer_key"],
                  consumer_secret=auth["consumer_secret"],
                  access_token_key=auth["access_token_key"],
                  access_token_secret=auth["access_token_secret"])

api.PostUpdate('...loading gossip xx')
