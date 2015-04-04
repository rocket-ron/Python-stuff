# Scramble - Assignment 2, part
# Write a scramble function that implements this algorithm.
#
# The scramble("12") should compute the scramble of "1", which is "1", interleaved with the scramble of "2", which is "2"
# The results is simply "12"
# The scramble of "1234" is the interleave of the scramble of "12", which is "12" and the scramble of "34", which is "34"
# The result is "1324"
# The scramble of 12345678 is 15372648
#------------------------------------------------------------------------------------
#
# Input: a string of arbitrary length
# Output: a scrambled representation of the string
#
# scramble(string):
# if length of string <= 2, return the string
# if length of string > 2, 
#   split the string -> string1 and string2
#   return interleave(scramble(string1) + scramble(string2))

import math


# interleave two equal length strings, or at most a length of 1 difference in lengths
# interleaving is defined as taking 1 character from each string, starting from the beginning
# of the string to the end, alternating from string1 to string2. 
def interleave(s1, s2):
	if (len(s1) + len(s2)) <= 2:
		return s1 + s2
	else:
		result = ""
		for i in range(0, min(len(s1), len(s2))):
			result += s1[i] + s2[i]

		# take care of the case that one sring is longer than the other by 1 character
		if len(s1) > len(s2):
			result += s1[len(s1)-1]
		elif len(s2) > len(s1):
			result += s2[len(s2)-1]
		return result

# scramble a string by splitting it into two halves and interleaving the halves
def scramble(s):
	if len(s) <= 2:
		return s
	else:
		ss = split(s)
		return interleave(scramble(ss[0]), scramble(ss[1]))


# split a string into two parts. If the string is odd length, the first "half" wil
# be 1 larger than the second "half"
def split(s):
	if len(s) > 2:
		if len(s) % 2 == 0:
			return (s[:len(s)//2], s[len(s)//2:])
		else:
			return (s[:len(s)//2+1], s[len(s)//2+1:])
	elif len(s) == 2:
		return(s[0], s[1])
	else:
		return(s, )

# determine the next power of 2 equal or larger to the length of the string
# and pad the string to that length.
def padToPowerOf2(input):
	i = 0
	size = len(input)
	while (math.pow(2,i) < size):
		i += 1
	return input + ' ' * (pow(2,i) - size)

s = str(input('Enter a string: '))
print(scramble(s))
print(scramble(padToPowerOf2(s)))
