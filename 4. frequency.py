import nltk
import pandas
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
f=open("sample.txt","r")
dataf=f.read().replace('\n',' ');
dataf=dataf.lower()
delimiters=['(',')',';',',','.','/']
for i in delimiters:
	dataf=dataf.replace(i,'')

data=word_tokenize(dataf)
n=input("Enter n:")
output=list(ngrams(data,pandas.to_numeric(n)))
print(output)