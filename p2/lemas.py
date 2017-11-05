#!/usr/bin/python3

import sys
import re
import math

text = []
unigrams = {}
bigrams = {}
V = 0

def main():
	process_files()
	
	smoothing = [False, True]
	message = ["SEM ALISAMENTO", "COM ALISAMENTO"]

	for i in range(0,2):
		print(message[i] + ":\n")
		for sentence in text:
			sentence = sentence.lower()
			
			scoreVir = sentence_odds(sentence, smoothing[i])
			scoreVer = sentence_odds(sentence.replace("vir", "ver"), smoothing[i])
			
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
			
			print("")
		print("\n\n")


def sentence_odds(sentence, smooth=False):
	words =  re.compile(r'[^a-zA-Z0-9\áéíóúàèìòùâêîôûãẽĩõũç\-]').split(sentence)
		
	# clean up empty words that showed up
	# FIXME: not cleaning up everything
	tmp = [word for word in words if len(word) > 0]
	
	for word in words:
		if word in unigrams:
			result = unigrams[word]
		else:
			unigrams[word] = 0
		
	
	sentence = ["<s>"] + words
	
	final_result = 0
	for i in range(1, len(sentence)):
		word1 = sentence[i-1]
		word2 = sentence[i]
		
		if not smooth:
			result = calc_bigram(word1, word2)
		else:
			result = calc_bigram_smooth_add_one(word1, word2)
		
		final_result = final_result + result
	
	return final_result


def calc_bigram(word1, word2):
	bigram = word1 + " " + word2
		
	if bigram not in bigrams:
		result = 0
	
	else:
		result = abs(math.log(bigrams[bigram]/ max(1, unigrams[word1])))
		#~ result = bigrams[bigram] / max(1, unigrams[word1])
	
	return result


def calc_bigram_smooth_add_one(word1, word2):
	bigram = word1 + " " + word2
		
	if bigram not in bigrams:
		result = 0
	
	else:
		result = abs(math.log(bigrams[bigram]/(unigrams[word1]+V)))
		#~ result = bigrams[bigram]+1 / (unigrams[word1] + V)
	
	return result


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
		
	global V
	V = len(unigrams)
	
	f = open(bigs_name, "r")
	for line in f.readlines():
		line.replace("\n", "")
		splits = line.split("\t")
		
		both_words = splits[0]
		count = int(splits[1])
		
		bigrams[both_words] = count
	

if __name__ == "__main__":
	main()
