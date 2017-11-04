#!/usr/bin/python3

import sys
import re

text = []
unigrams = {}
bigrams = {}

def main():
	process_files()
	
	for sentence in text:
		sentence = sentence.lower()
		
		print(sentence)
		
		words =  re.compile(r'[^a-zA-Z0-9\áéíóúàèìòùâêîôûãẽĩõũç\-]').split(sentence)
		print(words)
		
		# clean up empty words that showed up
		# FIXME: not cleaning up
		tmp = [word for word in words if len(word) > 0]
		
		for word in words:
			if word in unigrams:
				result = unigrams[word]
			else:
				unigrams[word] = 0
			
			#~ print(result, end=",")
		
		sentence = ["<s>"] + words
		
		# ERROR: NOT WORKING AT ALL, EVERYTHING IS 0
		for i in range(1, len(sentence)):
			bigram = sentence[i-1] + " " + sentence[i]
			
			if bigram not in bigrams:
				result = 0
			
			else:
				result = bigrams[bigram]
		
			print(bigram)
			print(result)
			
		print()
	
	

def process_files():
	args = sys.argv[1:]	
	unigs_name = args[0]
	bigs_name = args[1]
	param_name = args[2]
	tests_name = args[3]
	
	f = open(tests_name, "r")
	for line in f.readlines():
		text.append(line.replace("\n", ""))
	
	f = open(unigs_name, "r")
	for line in f.readlines():
		line.replace("\n", "")
		splits = line.split("\t")
		
		word = splits[0]
		count = int(splits[1])
		
		unigrams[word] = count
	
	f = open(bigs_name, "r")
	for line in f.readlines():
		line.replace("\n", "")
		splits = line.split("\t")
		
		both_words = splits[0]
		count = int(splits[1])
		
		unigrams[both_words] = count
	

if __name__ == "__main__":
	main()
