#!/usr/bin/python3

import fileinput
import re

word_counter = {}
bi_counter = {}
START_SYMBOL = "<s>"

def main():
	text = "";
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
		
		# dark magic to remove whitespaces
		# from https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
		line = ' '.join(line.split())
			
		text += line + "\n"
		
	get_unigrams(text)
	get_bigrams(text)

def get_unigrams(text):
	word_counter["<s>"] = 0
	
	for line in text.split("\n"):
		print(line)
		word_counter["<s>"] = word_counter["<s>"] + 1
		
		# split with regex
		words = re.compile(r'[^a-zA-Z0-9\áéíóúàèìòùâêîôûãẽĩõũç\-]').split(line)
		
		for w in words:
			if not w:
				continue
			
			if w not in word_counter:
				word_counter[w] = 1
			else:
				word_counter[w] = word_counter[w] + 1

	f_uni = open("virUnigramas.txt", "w");
	for word, count in sorted(word_counter.items()):
		f_uni.write("{}\t{}\n".format(word, count))

def get_bigrams(text):
	for line in text.split("\n"):
		
		# split with regex
		words = re.compile(r'[^a-zA-Z0-9\áéíóúàèìòùâêîôûãẽĩõũç-]').split(line)
		
		# special case: 1st word
		words = [START_SYMBOL] + words
		
		# might give problems with some stupid empty spaces that are not being rid of (whats their ascii code???)
		for i in range(1, len(words)):
			bigram = words[i-1] + " " + words[i]
			
			if bigram not in bi_counter:
				bi_counter[bigram] = 1
			else:
				bi_counter[bigram] = bi_counter[bigram] + 1
	
	f_bi = open("virBigramas.txt", "w");
	for bigram, count in sorted(bi_counter.items()):
		f_bi.write("{}\t{}\n".format(bigram, count))

if __name__ == "__main__":
	main()
