#!/usr/bin/python3

import sys
import re
import math

text = []
unigrams = {}
bigrams = {}

def main():
	process_files()
	
	for sentence in text:
		sentence = sentence.lower()
		
		scoreVir = sentence_ods(sentence)
		scoreVer = sentence_ods(sentence.replace("vir", "ver"))
		
		print(sentence)
		if scoreVir == scoreVer:
			print("Probabilidades iguais: " + str(scoreVir))
			print("Resultado: VIR (é o mais comum no corpus)")
		
		elif scoreVir >= scoreVer:
			print("Vir: {}, Ver: {}".format(str(scoreVir),str(scoreVer)))
			print("Resultado: VIR")
		
		else:
			print("Vir: {}, Ver: {}".format(str(scoreVir),str(scoreVer)))
			print("Resultado: VER")
		
		print()
		

def sentence_ods(sentence):
	words =  re.compile(r'[^a-zA-Z0-9\áéíóúàèìòùâêîôûãẽĩõũç\-]').split(sentence)
		
	# clean up empty words that showed up
	# FIXME: not cleaning up
	tmp = [word for word in words if len(word) > 0]
	
	for word in words:
		if word in unigrams:
			result = unigrams[word]
		else:
			unigrams[word] = 0
		
		#~ print(result, end=",")
	
	#~ sentence = ["<s>"] + words
	sentence = words
	
	final_result = 0
	for i in range(1, len(sentence)):
		word1 = sentence[i-1]
		word2 = sentence[i]
		bigram = word1 + " " + word2
		
		if bigram not in bigrams:
			result = 0
		
		else:
			#~ result = math.log(bigrams[bigram]/unigrams[word1])
			result = bigrams[bigram]/ max(1, unigrams[word1])
	
		#~ print(result, end=",")
		final_result = final_result + result
	
	return final_result

def process_files():
	args = sys.argv[1:]	
	unigs_name = args[0]
	bigs_name = args[1]
	param_name = args[2]
	tests_name = args[3]
	
	f = open(tests_name, "r")
	for line in f.readlines():
		line = line.replace("\n", "")
		text.append(line)
		
		#~ if "vir" in line:
			#~ text.append(line.replace("vir", "ver"))
	
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
		
		bigrams[both_words] = count
	

if __name__ == "__main__":
	main()
