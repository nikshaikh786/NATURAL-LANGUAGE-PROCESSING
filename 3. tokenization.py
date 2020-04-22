import nltk

from nltk.tokenize import sent_tokenize, word_tokenize

data="Greetings of the day. This is the second sentence"
print("line tokenization: \n")
print(sent_tokenize(data))
print("\nWord Tokenization: \n")
print(word_tokenize(data))