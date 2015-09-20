#!/usr/bin/python

import re
import nltk
from collections import Counter
from itertools import islice, izip
import collections
import sys, getopt
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.util import ngrams
from nltk import bigrams

def compute_bi_gram(ifile_name) :
	punctuations = re.compile(r'[-.?!":;)(|0-9]')
	word_list = re.split('\s+', open(ifile_name).read().lower())
	print 'Words in file:',len(word_list)
	words = (punctuations.sub("",word).strip() for word in word_list)

	print '-'*30

		
	print Counter(izip(words, islice(words, 1, None)))

def main(argv):
	inputfile = ''
	outputfile = ''
	try :
		opts,args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
	except getopt.GetoptError :
		print 'NLP_P1.py -i <input_file_name> -o <output_file_name>'
		sys.exit(2)
	for opt,arg in opts :
		if opt == '-h' :
			print 'NLP_P1.py -i <input_file_name> -o <output_file_name>'
		elif opt in ("-i","--ifile") :
			inputfile = arg
		elif opt in ("-o","--ofile") :
			outputfile = arg
	print 'Input file is ', inputfile 
	print 'Output file is ', outputfile
	compute_bi_gram(inputfile)

if __name__ == "__main__" :
	main(sys.argv[1:])
