# -*- coding: utf-8 -*-

from sys import argv

VOCALES = ['a', 'e', 'i', 'o', 'u', 'y']
CONSO_CONCAT_SPECIAL = { 'b': ['l'],
						 'c': ['l', 'h'],
						 'f': ['l', 'r'],
						 'g': ['l', 'r'],
						 'l': ['l'],
						 'p': ['l', 'r'],
						 'q': ['u'],
						 'r': ['r'],
						 't': ['r']
					}
CONSO_CONCAT = ['b', 'bl',
				'c', 'cl', 'ch',
				'd',
				'f', 'fl', 'fr',
				'g', 'gl', 'gr',
				'h',
				'j',
				'k',
				'l', 'll',
				'm',
				'n',
				'ñ',
				'p', 'pl', 'pr',
				'qu',
				'r', 'rr',
				's',
				't', 'tr',
				'v',
				'w',
				'x',
				'y',
				'z'
				]


def get_vowels(word):
	"""
	Obtains the vowels of the word.
	"""
	vowels = []
	if word[0] not in VOCALES:
		for letra in word:
			if letra in VOCALES and (letra not in vowels):
				vowels.append(letra)
	return vowels

def get_first_char(list_words):
	"""
	Returns the first character of every word in 'list' words
	"""
	first_chars= []
	for word in list_words:
		if word[0] not in VOCALES:
			if len(word) > 1:
				if word[0] in CONSO_CONCAT_SPECIAL.keys() and word[1] in CONSO_CONCAT_SPECIAL[word[0]]:
					first_chars.append(word[0] + word[1])
				else:
					first_chars.append(word[0])
			else:
				first_chars.append(word[0])
		else:
			first_chars.append(word[0])
	return first_chars

def vowel_conso_combinations(first_char, list_vowels):
	"""
	Returns a list of combinations using 'first_char' with the vowels in
	the 'list_vowels' that are legal in Spanish.
	"""
	combinations= []
	for vowel in list_vowels:
		if first_char in CONSO_CONCAT:
			# print first_char + vowel
			combinations.append(first_char + vowel)
	return combinations

def generate_combinations(dic_syllable):
	"""
	Generate syllable combinations.
	"""
	root_list= dic_syllable[0]
	for i in range(1, len(dic_syllable.keys())):
		previus= len(root_list)
		# Necesitamos tener n copias de lo que hemos generado ya
		# donde n es el número de sílabas del nivel actual
		root_list = root_list * len(dic_syllable[i])
		for j in range(len(dic_syllable[i])):
			for k in range(previus):
				root_list[previus * j + k] = root_list[previus * j + k] + dic_syllable[i][j] 

	return root_list

def main(lis):
	if len(lis) > 1:
		print "$ Generating combinations ...\n"
		dic_combinations = {}
		first_chars = get_first_char(lis)
		composite_name= ""
		i = 0
		# Obtenemos combinaciones de vocales
		for pos in range(len(first_chars)):
			if first_chars[i] in VOCALES:
				dic_combinations[i] = [first_chars[i]]
				i += 1
			else:	
				vowels = get_vowels(lis[pos])
				if len(vowels) > 0:
					dic_combinations[i] = vowel_conso_combinations(first_chars[i], vowels)
					i += 1
	
		resultados = generate_combinations(dic_combinations)
		print "$ Generated %d combinations: " % len(resultados)
		for pos in range(len(resultados)):
			print "   - %s" % resultados[pos]	
	else:
		print "$ Not enough words, type at least 2."

if __name__ == '__main__':
	main(list(argv)[1:])
