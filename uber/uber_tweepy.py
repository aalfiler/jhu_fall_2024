import tweepy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# Twitter API credentials
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Function to clean tweets
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

# Function to get tweets
def get_tweets(query, count=100):
    tweets = []
    try:
        # Fetch tweets
        fetched_tweets = api.search_tweets(q=query, count=count)
        for tweet in fetched_tweets:
            cleaned_tweet = clean_tweet(tweet.text)
            tweets.append(cleaned_tweet)
        return tweets
    except tweepy.TweepError as e:
        print("Error : " + str(e))

# Get tweets about Uber
tweets = get_tweets("Uber", count=500)

# Combine all tweets into a single string
text = ' '.join(tweets)

# Generate word frequency
word_freq = Counter(text.split())

# Remove common words
stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'are', 'uber'])
word_freq = {word: count for word, count in word_freq.items() if word.lower() not in stop_words}

# Create and generate a word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Uber Technologies Sentiment Analysis from Twitter')
plt.tight_layout(pad=0)

# Save the image
plt.savefig('uber_sentiment_wordcloud_twitter.png', dpi=300, bbox_inches='tight')
plt.close()

print("Word cloud image has been saved as 'uber_sentiment_wordcloud_twitter.png'")