# Words With Friends (WWF) Cheat

alphabet = ['A','B','C','D','E','F','G','H','I','J','K',
			'L','M','N','O','P','Q','R','S','T','U','V',
			'W','X','Y','Z']
score = {"a": 1, "b": 4, "c": 4, "d": 2, "e": 1, "f": 4, 
         "g": 3, "h": 3, "i": 1, "j": 10, "k": 5, "l": 2, 
         "m": 4, "n": 2, "o": 1, "p": 4, "q": 10, "r": 1, 
         "s": 1, "t": 1, "u": 2, "v": 5, "w": 4, "x": 8, 
         "y": 3, "z": 10, "A": 0, "B": 0, "C": 0, "D": 0,
         "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
         "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, 
         "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0,
         "W": 0, "X": 0, "Y": 0, "Z": 0}

# Take all WWF words from enable1.txt and turn into a Python list.
# 1. Create an empty list
# 2. Open dictionary word list text file
# 3. For each word in the file, append it to the word list
# 4. Close the file

wordlist = []

f = open("enable1.txt", "r")
for line in f:
	line = line.strip()
	wordlist.append(line)
	
f.close()

# Get the WWF rack from the command line.
# 1. Import the sys module
# 2. Save the rack command line argument to a variable.

import sys
rack = sys.argv[1].lower()

# Build conditional statement if there are blanks
# 1. Count the number of available blanks in rack
# 2. Remove them from the rack

num_blanks = rack.count("?")
if "?" in rack:
	rack = filter(lambda a: a!="?", rack)
	
	# Create a list of possible racks if 1 or 2 blanks are present 
	rack_set1 = []
	rack_set2 = []
	rack_try1 = ""
	rack_try2 = ""
	for abc in alphabet:
		rack_try1 += abc 
		rack_try1 += rack
		rack_set1.append(rack_try1)
		rack_try1 = ""
	# Identify the rack list to be used for determining word 
	# candidates 
	if num_blanks == 2:
		for rack_try in rack_set1:
			for abc in alphabet:
				rack_try2 += abc 
				rack_try2 += rack_try
				print rack_try2
				rack_set2.append(rack_try2)
				rack_try2 = ""
		rack_set = rack_set2
	else:
		rack_set = rack_set1
else:
	rack_set = [rack]

print num_blanks
print rack_set

# Find all of the valid WWF words that can be made up of the letters in 
# the rack.
# 1. Set up a for loop to go through every word in wordlist
# 2. Use a variable to keep track of whether or not the word is still a 
#    candidate for this rack
# 3. Set up a nested for loop to go through every letter in the word
# 4. If a letter isn't found in the rack, DISQUALIFY the word
# 5. If a letter is found in the rack REMOVE the letter from the rack
#    and keep going 
# 6. If we've gone through all of the letters in the word and we still 
#    have a candidate, it's a MATCH for this rack!

valid_words = []	
for rack_test in rack_set:	
	for word in wordlist:
		candidate = True
		rack_letters = list(rack_test)
		word_score = ""
		for letter in word:
			if letter in rack_letters: 
				rack_letters.remove(letter)
				word_score += letter
			elif letter.upper() in rack_letters:
				rack_letters.remove(letter.upper())
				word_score += letter.upper()
			else:
				candidate = False
		for entry in valid_words:
			if word_score == entry[1]:
				candidate = False
		if candidate == True:
			# Get the Scrabble scores for each word.
			# 1. Use a variable to keep track of the running value of 
			#    the word.
			# 2. For each letter in the word, look up the letter value 
			#    and add it to the total.
			total = 0
			for letter in word_score:
				total = total + score[letter]
			if total > 0:
				valid_words.append([total, word_score])
# Print the valid words, sorted by Scrabble score.
# 1. Use a list to keep track of the valid words.
# 2. Save both the word and word score to that list.
# 3. Sort the list, i.e. [[10, "a"], [20, "b"], [30, "c"]].
# 4. For each entry in the sorted list print the score and word.

valid_words.sort()

for entry in valid_words:
	score = entry[0]
	word = entry[1]
	print str(score) + " " + word





