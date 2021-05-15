from collections import Counter

str1 = input('Enter word 1: ')
str2 = input('Enter word 2: ')

def anagram_maker(str1, str2):
	dict1 = Counter(str1)
	dict2 = Counter(str2)

	keys1 = dict1.keys()
	keys2 = dict2.keys()

	count1 = len(keys1)
	count2 = len(keys2)

	set1 = set(keys1)
	common_keys = len(set1.intersection(keys2))

	if common_keys == 0:
		return count1 + count2
	else:
		return ((count1 + count2) - (common_keys * 2))

print(anagram_maker(str1, str2))



# if __name__ == "__main__":
#	str1 = 'yuka'
#	str2 = 'chris'
#	print (anagram_maker(str1, str2))
