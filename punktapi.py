import nltk
from nltk.corpus import state_union
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize


train_text = "Shooting is a very popular sport. Hunters use guns to shoot animals. Terrorists also use them to kill"
sample_text = "Sharpshooter Mark shoots a dangerous animal with a gun"


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

#tokenized = sent_tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			chunkGram = r""" Chunk: {<RB. ?> * <VB. ?> * <NNP. ?>+ <NN>?}"""
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			chunked.draw()
	except Exception as e:
		print(str(e))

process_content()
