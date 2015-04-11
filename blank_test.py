import sys

alphabet = ['A','B','C','D','E','F','G','H','I','J','K',
			'L','M','N','O','P','Q','R','S','T','U','V',
			'W','X','Y','Z']
			
rack = sys.argv[1].lower()
rack_letters = list(rack)

# Build conditional statement if there are blanks
# 1. Count the number of available blanks in rack
# 2. Remove them from the rack

if "?" in rack_letters:
	num_blanks = rack_letters.count("?")
	rack_letters = filter(lambda a: a!="?", rack_letters)
	
	# Create a list of possible racks if 1 or 2 blanks are present 
	rack_set1 = []
	rack_set2 = []
	rack_try1 = []
	rack_try2 = []
	for abc in alphabet:
		rack_try1.append(abc) 
		rack_try1.extend(rack_letters)
		rack_set1.append(rack_try1)
		rack_try1 = []
	# Identify the rack list to be used for determining word 
	# candidates 
	if num_blanks == 2:
		for rack_try in rack_set1:
			for abc in alphabet:
				rack_try2.append(abc) 
				rack_try2.extend(rack_try)
				print rack_try2
				rack_set2.append(rack_try2)
				rack_try2 = []
		rack_set = rack_set2
	else:
		rack_set = rack_set1
else:
	rack_set = [rack_letters]
print num_blanks
print rack_set
