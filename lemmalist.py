import nltk

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print("rocks: ", lemmatizer.lemmatize("rocks"))
print("corpora: ", lemmatizer.lemmatize("corpora"))

lem = ["feet","given","Given","giver","gives","gave"]

for word in lem:
	print(word + " : "+ lemmatizer.lemmatize(word))