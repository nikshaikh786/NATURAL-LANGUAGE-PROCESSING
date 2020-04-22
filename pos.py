import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words=set(stopwords.words('english'))
stop_words.add(';')
stop_words.add(':')
stop_words.add('.')
stop_words.add(',')
f=open("sample.txt","r")
data=f.read()
tokenized=sent_tokenize(data)
for i in tokenized:
	wordsList=nltk.word_tokenize(i)
	wordsList=[w for w in wordsList if not w in stop_words]
	tagged=nltk.pos_tag(wordsList)
	print(tagged)