import nltk

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print("\n=====================\n")
print("WoedNet Lemmatizer on a sentence")
sentence = "The striped bats are hanging on their feet for best view of the inverted worlds"

word_list = nltk.word_tokenize(sentence)
print(word_list)

lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
print(lemmatized_output)


