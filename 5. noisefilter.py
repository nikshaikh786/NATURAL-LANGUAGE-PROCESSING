import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

f=open('sample.txt','r')
data=f.read().replace('\n', ' ')

print(data)
noise=['{','}','!']

for i in noise:
	data=data.replace(i, '')

print(data)