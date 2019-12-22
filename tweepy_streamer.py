from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials as tc

#### TWITTER STREAMER ####
class TwitterStreamer():
	"""
	Class for streaming and processing live tweets
	"""

	def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
		# This handles twitter authentication and the connection to the Twitter Streaming API
		listener = TwitterListener()
		auth = OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
		auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

		stream = Stream(auth, listener)

		stream.filter(track=hash_tag_list)

#### TWITTER STREAM LISTENER ####
class TwitterListener(StreamListener):
	"""
	This is a basic listener class that just prints recieved tweets to stdout
	"""

	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename


	def on_data(self, data):
		try:
			print(data)
			with open(self.fetched_tweets_filename, 'a') as tf:
				tf.write(data)
			return True
		except BaseException as e:
			print("Error on data: %s" %str(e))
		return True

	def on_error(self, status):
		print(status)

if __name__ == "__main__":

	hash_tag_list = ["donald trumph", "srk", "barack obama"]
	fetched_tweets_filename = "tweets.json"

	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)###