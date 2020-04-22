__author__ = 'Shadab Shaikh'
__title__ = 'Spell checking using pyspellchecker'
__date__ = '25-02-2020'
__version__ = '1.0'

print('Author		: ' + __author__)
print('Title		: ' + __title__)
print('Date		: ' + __date__)
print('Version		: ' + __version__)

from spellchecker import SpellChecker

str1=""
spell = SpellChecker()

while(str1!="No"):
	str1=input("\nEnter your word here| No to exit\t")

	misspelled = spell.unknown([str1])
	if(len(misspelled)==0):
		print("\nSpelling is correct")

	for word in misspelled:
		print("\nShowing most likely corrected spelling\n")
		print(spell.correction(word))
		if(len(spell.candidates(word))>=2):
			print("\nDid you mean?\n")
			print(spell.candidates(word))