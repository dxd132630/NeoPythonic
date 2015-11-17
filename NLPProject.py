
# import statements
from __future__ import division
import nltk
from nltk import FreqDist
from nltk.corpus import wordnet as wnet
from nltk.corpus import brown as b
import math
import numpy as np
import sys
import re
from itertools import islice, izip
from nltk.probability import *
from collections import defaultdict
import collections
import sys, getopt


# Constants used in refernece to the Sentence similarity computation as mentioned in "Sentence Similarity Based on Semantic Nets and Corpus Statistics, IEEE TRANSACTIONS ON KNOWLEDGE AND DATA ENGINEERING gernal VOL. 18, NO. 8, AUGUST 2006" gernal 

ALPHA = 0.2
BETA = 0.45
ETA = 0.4
PHI = 0.2
DELTA = 0.85

brown_freqs = defaultdict(lambda: 0)
N =0 
def indexNumbering(T_words, T_joint, T_index):
	print T_words
	print T_joint
	print T_index
	r1 = np.zeros(len(T_joint))
	i = 0
	T_set = set(T_words)
	for T_j in T_joint:
		if T_j in T_set:
			r1[i] = T_index[T_j]
		else:
			r1[i] = 0
	        i = i + 1
	print r1
	return r1
	
def word_order_info(s1,s2):
	T1 = nltk.word_tokenize(s1)
	T2 = nltk.word_tokenize(s2)
	T = list(set(T1).union(set(T2)))
	T_indice = {t[1]:t[0] for t in enumerate(T)}
	r1 = indexNumbering(T1, T, T_indice)
	r2 = indexNumbering(T2, T, T_indice)
	return (1.0 - DELTA) * (np.linalg.norm(r1 - r2) / np.linalg.norm(r1 + r2))
	
def ic(w) :
	total = 0
	for sentence in b.sents():
		for word in sentence:
			total = total + 1
			brown_freqs[word.lower()] +=1
	
	print w.lower() ,":",brown_freqs[w.lower()], 1.0 - (math.log(brown_freqs[w.lower()]) / math.log(total+1))
    
def sentSimilarity(s1,s2):
	print s1,"--------->",s2
	word_order_info(s1,s2)
	w1 = nltk.word_tokenize(s1)
	w2 = nltk.word_tokenize(s2)
	for w in w1:
		ic(w)
	
def batchProcessSentences(file_name) :
	sent_pairs = [] 
	with open(file_name) as input:
    		for line in input :
			sent_pairs.append(line.split('\t'))
	print sent_pairs
	for sent in sent_pairs:
		sentSimilarity(sent[0],sent[1])
def main(argv):
	inputfile = ''
	stmt1 = ''
	stmt2 = ''
	batch = None
	try :
		opts,args = getopt.getopt(argv, "hi:1:2:",["ifile=","ofile=","sent1=","sent2="])
	except getopt.GetoptError :
		print 'python NLPFinalProject.py -i <input_file_name>'
		sys.exit(2)
	for opt,arg in opts :
		if opt == '-h' :
			print 'python NLPFinalProject.py -i <input_file_name>'
			print 'python NLPFinalProject.py -1 <sentence1> -2 <sentence2>'
		elif opt in ("-i","--ifile") :
			batch = True
			inputfile = arg
		elif opt in ("-1","--sent1") :
			stmt1 = arg
		elif opt in ("-2","--sent2") :
			stmt2 = arg
	if batch == True :
		batchProcessSentences(arg)
	else :
		sentSimilarity(stmt1,stmt2)

if __name__ == "__main__" :
	if len(sys.argv) == 1 :
		print ' Invalid number of arguments'
	else :
		main(sys.argv[1:])


