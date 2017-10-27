#!/usr/bin/python3

import fileinput
import re

word_counter = {}
for line in fileinput.input():
	
	# remove some punctuation we dont want
	line = re.sub(r"\.|,|!|\?|\n|«|»|(|)", "", line)
	
	# clean up sentence
	line = line.lower()
	line = line.strip()
	
	
	# replace temporarily (this most likely means forever)
	#~ line = line.replace("á", "a")
	#~ line = line.replace("é", "e")
	#~ line = line.replace("í", "i")
	#~ line = line.replace("ó", "o")
	#~ line = line.replace("ú", "u")
	
	# split with regex
	words = re.compile(r'[^a-zA-Z0-9\áéíóúàèìòùâêîôûãẽĩõũç-]').split(line)
	
	#~ print(line)
	#~ print()
	#~ print(words)
	
	for w in words:
		if not w:
			continue
		
		if w not in word_counter:
			word_counter[w] = 1
		else:
			word_counter[w] = word_counter[w] + 1

for word, count in sorted(word_counter.items()):
	print("{}\t{}".format(word, count))
    
