### Author: Sonal Doomra
### UMID: 88529245
### Purpose: 507 Waiver

### Part 1: Create a program to analyze the twitter timeline of a selected user
import tweepy
import nltk
import json
import sys

my_consumer_key = "MmyAQjiDss3cSSSR5hiWe2hJU"
my_consumer_secret = "5LfzwPfBZTaDI1AgaY8eBoPsZ6h3T6Ux1Sqp5W8KQMOdEmvNY5"

auth = tweepy.OAuthHandler(consumer_key = my_consumer_key, consumer_secret = my_consumer_secret)
auth.set_access_token("928092520860536832-RialPNxhpN7XtXCIcloGjtykeLGWv3K", 
						"jrfduRU5qdcPOiBW8lfPPSgjC5p1QyFK6uWndyjKTYRGx")


api = tweepy.API(auth) #To get the authenticated interface object

# this function analyzes the given number of tweets for the given user a
def analyze(user_name, number_of_tweets):
	user = api.get_user(user_name) # Get the user

	print("USER:" + user.screen_name)
	print("TWEETS ANALYZED: " + number_of_tweets)

	orig_tweets = []

	#Get the original tweets
	for tweet in api.user_timeline(screen_name = user.screen_name, count = number_of_tweets):
	    if not tweet.text.startswith('RT'):
	    	orig_tweets.append(tweet)
	
	#make multiple calls to analyze the tweets with different parts of speech
	analyze_tweets(orig_tweets, "verbs")
	analyze_tweets(orig_tweets, "nouns")
	analyze_tweets(orig_tweets, "adjectives")

	# Print original tweets count
	count_orig = len(orig_tweets)

	print("ORIGINAL TWEETS: " , count_orig)

	sum_favcount = 0
	sum_retweetcount = 0

	for orig_tweet in orig_tweets:
		sum_favcount += orig_tweet.favorite_count
		sum_retweetcount += orig_tweet.retweet_count

	print("TIMES FAVORITED (original tweets only):" ,sum_favcount)
	print("TIMES RETWEETED (original tweets only):" ,sum_retweetcount)

#this function analyzes the original tweets for different parts of speech
def analyze_tweets(orig_tweets, part_of_speech):
	if part_of_speech.lower() == "verbs":
		keyword = "VB"
	elif part_of_speech.lower() == "nouns":
		keyword = "NN"
	else:
		keyword = "JJ"

	list_of_words = [] # list of words to be analyzed
	for tweet in orig_tweets:
		tokens = nltk.word_tokenize(tweet.text)
		tagged = nltk.pos_tag(tokens)
		length = len(tagged)
		for (key,value) in tagged:

			if ord(key[0]) not in range(ord('A'), ord('z')) or key.startswith("http") or key.startswith("https"):
				continue
			if value.startswith(keyword):
				list_of_words.append(key)

	word_counts = {}		#dictionary of words to be analyzed

	for words in list_of_words:
		words = words.lower()
		if words in word_counts:
			word_counts[words] += 1
		else:
			word_counts[words] = 1

	sorted_words = sorted(word_counts.items(), key = lambda x : x[1], reverse = True)

	print(part_of_speech.upper() +":")
	for i in range(5): # print only top 5 from sorted list of words
		print(sorted_words[i])

def main(argv):
	user_name = argv[1]
	number_of_tweets = argv[2]
	analyze(user_name, number_of_tweets)


if __name__ == '__main__':
    main(sys.argv)
