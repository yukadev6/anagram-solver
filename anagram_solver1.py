from collections import Counter

str1 = input('Enter word 1: ')
str2 = input('Enter word 2: ')

def anagram_maker(str1, str2):
	dict1 = Counter(str1)
	dict2 = Counter(str2)

	keys1 = dict1.keys()
	keys2 = dict2.keys()

	count1 = len(str1)
	count2 = len(str2)

	set1 = set(keys1)
	common_keys = len(set1.intersection(keys2))

	if common_keys == 0:
		print("number of letters to create anagrams:", count1 + count2)
		print("word 1 anagram:", str1 + str2)
		print("word 2 anagram:", str2 + str1)
	elif common_keys == count1 and common_keys == count2:
		print("The two words are already anagrams!")
	else:
		print("number of letters to create anagrams:", ((count1 + count2) - (common_keys*2)))
		print("Try adding the missing letters to each word to create anagrams!")


anagram_maker(str1, str2)
