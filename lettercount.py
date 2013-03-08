# opens the text file from user input and reads it, which means it creates one string that has all of the contents of the file, though it does preserve the new lines and other formatting
#text = open(raw_input("Type in the .txt filename > ")).read()


# import text file name to use for then piping to the spark utility to get a graph
from sys import argv

script, textFile = argv

text = open(textFile).read()

'''
Two ways to run this program:
1. We could keep separate counters for each letter, so that at the end you'd just have a loop that printed the letter of the alphabet with the count for that particular letter
2. we could loop through the entire text 26 times, just printing whenever we had the final total
3. Use a list instead to minimize number of loops
'''

"""
# This is method 1, which also uses ord to get the alphabet instead of importing it

# this is a for loop to create 26 counter variables per letter
# ord('a') returns unicode numeric for that letter, then we have it ending it ord('z)+1 to make sure to include z, so the below range is equivalent to range(unicode # for a, unicode number for z + 1) so that we can use a for loop and increment by 1 numerically each time

# creating a dictionary where the keys are each letter and the values will eventually be the count but to start with we're setting them to 0
counts = {}
for x in range(ord('a'),(ord('z')+1)):
	# globals is a function to return a dictionary of the current global namespace, keys are the names, values are the value for the name
	# variableName = 2 is the same thing as globals()["variableName"] = 2
	# chr(x) converts the ordinal position in the alphabet back into a string of the equivalent letter to use for the variable name
	# globals()['count' + chr(x)] = 0
	counts[chr(x)] = 0

# goes through each letter in the opened text file, finds that letter as a key in the counts dictionary, increments the value by 1
# need to find some way to strip the text file of non-alphabet characters
for letter in text:
	if ord(letter.lower()) in range(ord('a'),(ord('z')+1)):
		counts[letter.lower()] += 1
	else:
		pass

print counts
"""

"""
# This is method 2, which also uses the imported string module to get the alphabet rather than using ord

# importing string module to be able to get in alphabet
import string

# creating a list that contains the entire alphabet in lowercase, this print ["abcd..."]
alphabet = string.lowercase

# for loop to go through each item (letter) in the alphabet list
for letter in alphabet:
	# set a counter variable to 0 each time we count a new letter
	counter = 0

	# for loop to go through each item (character) in the string "text"
	for char in text: 
		# convert each item (character) to lowercase and compare it to the letter in the alphabet we're currently counting for
		if char.lower() == letter: 	
			# if the character is the letter we're counting up, increase the counter by 1
			counter += 1

	# now that we've counted all occurrences of the particular letter in question, print how many occurrences there are
	print counter
"""

# This is method 3, to use a list with minimum number of loops

# initialize a list that will keep track of the count of letter occurrences in the order of the alphabet, preset it to have 26 0s
alphacount = [0] * 26

# this was used to track number of loops that we went through
# loopCount = 0

# for loop to go through each and every single character in the text
for char in text:
	# if the character, when converted into a lowercase letter, is a letter (as defined by the numeric range that lowercase letters fall into, then run the next line
	# .lower doesn't change anything if it's not a letter or is already lowercase
	if ord(char.lower()) in range(ord('a'),(ord('z')+1)):
		# increment the value at the position in the list
		alphacount[ord(char.lower())-ord('a')] +=1
	#loopCount += 1

#print "this is the final count list: " , alphacount

#print "this is the total number of loops: " , loopCount

#print "this is the number of characters in the file: " , len(text)