from Credentials import Credentials
from tweepy import OAuthHandler

# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

	def authenticate_twitter_app(self):
		credentials = Credentials()
		twitter_credentials = credentials.twitter()
		auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
		auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
		return auth
