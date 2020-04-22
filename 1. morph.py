from nltk.corpus import wordnet


synonyms=[]
for syn in wordnet.synsets('Luncheon'):
	for lemma in syn.lemmas():
		synonyms.append(lemma.name())

print(synonyms)