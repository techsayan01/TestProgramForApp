from flask import Flask
from app import *

import json
from authenticator.TwitterAuthenticator import TwitterAuthenticator
from streamer.TwitterClient import TwitterClient
from analyzer.TweetAnalyzer import TweetAnalyzer 

import numpy as np
import utils

@app.route('/tweets/', methods=['GET'])
def tweets():
	try:
		source = request.args.get('source')
		twitter_client = TwitterClient()
		tweet_analyzer = TweetAnalyzer()
		result = []
		tweet = {}

		if  source[0] == '#':
			source = source[1:]
			api = twitter_client.get_twitter_client_api()
			tweets = api.user_timeline(screen_name=str(source), count=1,tweet_mode = 'extended')

			for info in tweets[:3]:
				tweet_id = info.id
				created_at = info.created_at
				full_text = info.full_text
				tweet = {
					"id" : str(tweet_id),
					"full_text" : str(full_text),
					"created_at": str(created_at)
				}
				result.append(tweet)
			print(result)

		elif source[0] == '@':
			source = source[1:]
			twitter_client = TwitterClient(str(source))
			tweets = twitter_client.get_user_timeline_tweets(1)
			for info in tweets[:3]:
				tweet_id = info.id
				created_at = info.created_at
				full_text = info.text
				tweet = {
					"id" : str(tweet_id),
					"full_text" : str(full_text),
					"created_at": str(created_at)
				}
				result.append(tweet)
			print(result)

		else:
			result = {"error" : "Out of scope"}

		return json.dumps(result)

	except:
		print('Not A valid url')	
