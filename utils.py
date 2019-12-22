def formatter(value):
	
	tweet_id = value.id
	created_at = value.created_at
	full_text = value.text
	tweet = {
		"id" : str(tweet_id),
		"full_text" : str(full_text),
		"created_at": str(created_at)
	}
	return tweet