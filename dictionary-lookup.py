# Usage:
# $ python3 dictionary-lookup.py azattyk

import sys, re

# take the first argument from the command line 
word = sys.argv[1]

# internal list for holding the dictionary
dict = []

# read in the dictionary, line by line
for line in open('mydictionary.tsv', 'r').readlines():
	# discard lines that have no content or are comments
	line = line.strip()
	if line == '':
		continue
	if line[0] == '#':
		continue

	# process file to replace spaces with tabs
	line = re.sub('  +', ' ', line)
	line = line.replace(' ', '\t', 3)
	row = line.split('\t')
	
	# add the line to the internal dictionary
	dict.append(row)

# go through the dictionary and look up the word
for w in dict:
	if w[0] == word or w[1] == word or w[2] == word:
		# print out the definition
		print('Definition:', w[3])


