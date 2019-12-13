"""
Same as wordCloud.ipynb on Colab, just runs locally to more easily save the images
"""

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
# % matplotlib inline


df = pd.read_csv('data.csv', header=0, delimiter=',', index_col=0)

text = df.text[2]

# Create and generate a word cloud for one sentence
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

text = " ".join(sentence for sentence in df.text)
print ("There are {} words in the combination of all sentences.".format(len(text)))

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["the", "pro", "ana"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


proAna = " ".join(sentence for sentence in df[df["label"]==1].text)

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(proAna)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud.to_file("pro-ana-cloud.png")

proRecovery = " ".join(sentence for sentence in df[df["label"]==0].text)

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(proRecovery)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud.to_file("pro-recovery-cloud.png")
