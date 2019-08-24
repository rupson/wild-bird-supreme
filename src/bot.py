import twitter
import json
import LanguageCore

with open("auth.json", "r") as authFile:
    auth = json.load(authFile)

api = twitter.Api(consumer_key=auth["consumer_key"],
                  consumer_secret=auth["consumer_secret"],
                  access_token_key=auth["access_token_key"],
                  access_token_secret=auth["access_token_secret"])


def main():
    tweetCandidate = LanguageCore.compose_tweet()
    print(tweetCandidate, "\n")
    adminRes = str(
        input("Send tweet: Y\nGenerate new: N\nQuit: Any other key\n")).upper()
    if adminRes == "Y":
        api.PostUpdate(tweetCandidate)
        return False
    elif adminRes == "N":
        return True
    else:
        return False


if __name__ == "__main__":
    while main() == True:
        continue
