#importing chunk library from nltk
import nltk
from nltk import ne_chunk

text = "Reliance's CEO Mr.Mukesh Ambani Introduced the new JIO services at Brabourne Stadium Centre, Boston, USA"

#tokenize and POS Tagging before doing chunk
token = nltk.word_tokenize(text)
tags = nltk.pos_tag(token)

#identify named entities to create chunks
chunk = ne_chunk(tags)
print("Input text is :", text)
print("Chunk output is ")
print(chunk)

#generate the parse tree
chunk.draw()
