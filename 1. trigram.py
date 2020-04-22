import nltk
from nltk import trigrams
from nltk.tokenize import word_tokenize
f=open("sample.txt","r")
dataf=f.read().replace('\n',' ');
delimiters=['(',')',';',',','.','/']
for i in delimiters:
	dataf=dataf.replace(i,'')
print(dataf)
data=word_tokenize(dataf)

trigrams=list(trigrams(data))
print(trigrams)
print('\n')
