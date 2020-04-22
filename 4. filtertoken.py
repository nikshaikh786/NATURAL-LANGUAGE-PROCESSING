import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data="Greetings of the day"
print("Sentences:\n")

word_tokens=word_tokenize(data)
print(word_tokens)

print("\n Filtered Sentences: \n")
stop_words = set(stopwords.words('english'))
filtered_sentences = [w for w in word_tokens if not w in stop_words]

print(filtered_sentences)
print("\n Stop Words: \n")
print(stop_words)