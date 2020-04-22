import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize
f=open("sample.txt","r")
dataf=f.read().replace('\n',' ');
delimiters=['(',')',';',',','.','/']
for i in delimiters:
	dataf=dataf.replace(i,'')
print(dataf)
data=word_tokenize(dataf)


grams=list(ngrams(data,4))
print(grams)