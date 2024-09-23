import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Dictionary of words and their frequencies
word_freq = {
    'Innovation': 25,
    'Convenience': 22,
    'Disruption': 18,
    'Controversy': 16,
    'Gig-economy': 15,
    'Regulation': 14,
    'Competition': 13,
    'Technology': 12,
    'Growth': 11,
    'Challenges': 10,
    'Ridesharing': 9,
    'Expansion': 8,
    'Driver-issues': 7,
    'Market-leader': 6,
    'Profitability': 5,
    'User-experience': 4,
    'Safety': 3,
    'Sustainability': 2,
    'Future-mobility': 1
}

# Create and generate a word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Uber Technologies Sentiment Analysis')
plt.tight_layout(pad=0)

# Save the image
plt.savefig('uber_sentiment_wordcloud.png', dpi=300, bbox_inches='tight')
plt.close()

print("Word cloud image has been saved as 'uber_sentiment_wordcloud.png'")