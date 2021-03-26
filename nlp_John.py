from textblob import TextBlob
import nltk

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

# print(blob.word_counts["juliet"])
# print(blob.word_counts["romeo"])
# print(blob.word_counts["thou"])
# print(blob.words.count("joy"))
# print(blob.noun_phrases.count("lady capulet"))

stops = stopwords.words("english")

more_stop_words = ["thee", "thy", "thou"]
stops += more_stop_words

items = blob.word_counts.items()
# print(items)

items = [item for item in items if item[0] not in stops]

# print(items[:10])

from operator import itemgetter

sorted_items = sorted(items)
# print(sorted_items[:10])

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
# print(sorted_items[:10])

top_20 = sorted_items[:20]

# print(top_20)

df = pd.DataFrame(top_20, columns=["words", "count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(
    x="words", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"]
)
plt.gcf().tight_layout()
plt.show()

import imageio
from wordcloud import WordCloud

mask_image = imageio.imread("images\mask_heart.png")
text = Path("RomeoAndJuliet.txt").read_text()

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")