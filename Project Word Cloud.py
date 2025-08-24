import pandas as pd
import re
from wordcloud import STOPWORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#let's load the IMDB dataset
df = pd.read_csv("IMDB-Dataset.csv")
print(df.head())

print(df.columns)
print(df['review'][0])

text = ' '.join(df['review'].astype(str).tolist()) #converting to string, turning into list and joining them
text = re.sub(r'[^A-Za-z\s]','',text)  #removing punctuation marks and numbers
text = re.sub(r'<.*?>', '', text)  
text = text.lower() #to lowercase

stopwords = set(STOPWORDS) #converting defualt STOPWORDS into set
text = ' '.join(word for word in text.split() if word not in stopwords) #ensuring text contains meaningfull words after removing words that are in stopwords

wordcloud = WordCloud(width=800, height=400,background_color='white').generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title("IMDB Movie Reviews Word Cloud")
plt.show()

#saving the image
wordcloud.to_file("imbd_wordcloud.png")
