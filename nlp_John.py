from textblob import TextBlob

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd
import collections
from wordcloud import WordCloud

from operator import itemgetter

# Read the file
blob = TextBlob(Path("book of John text.txt").read_text())

# Create a function to hold the boolean for the nouns
is_noun = lambda pos: pos[:2] == "NN"
noun_list = [word.lower() for (word, word_type) in blob.tags if is_noun(word_type)]

# Create a string to hold the nouns
noun_words = ""

for i in noun_list:
    noun_words += i + " "

# Create new Text blob with the noun words
new_blob = TextBlob(noun_words)

# Remove all stopwords
stops = stopwords.words("english")

# Add new stop words
more_stop_words = [
    "thee",
    "thy",
    "thou",
    "thy",
    "ye",
    "verily",
    "thee",
    "hath",
    "say",
    "thou",
    "art",
    "shall",
    "saith",
    "therefore",
]
stops += more_stop_words

# Count word frequency
items = new_blob.word_counts.items()
items = [item for item in items if item[0] not in stops]

# Sort the words based on their frequencies and convert to a dictionary
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
top_15 = sorted_items[:15]
top_15_dict = dict(top_15)

# Generate the Word cloud based on the top 15 words
wordcloud = WordCloud(colormap="terrain", background_color="salmon")
wordcloud = wordcloud.generate_from_frequencies(top_15_dict)
wordcloud = wordcloud.to_file("BookOfJohn.png")
