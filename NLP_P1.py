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
from operator import itemgetter

def compute_bi_gram(ifile_name,ofile_name) :
	words = re.findall('\w+',open(ifile_name).read())	
	words = [word.lower() for word in words]	
	c = Counter(zip(words, islice(words, 1, None)))
	with open(ofile_name, 'a') as f:
    		for k,v in c.items():
			temp = str(k)+str(v)
        		f.write(str(temp))
			f.write("\n")
	print 'Model build!'

def compute_bi_gram_for_stmt(stmt,ofile_name) :
	print '-'*50
	words = re.findall('\w+',stmt)
	words = [word.lower() for word in words]
	with open(ofile_name,'rt') as f:
		for line in f :
			print line
			for i in range(0,len(words)):
				w1 = words[i]
				for j in range(0,len(words)):
					w2 = words[j]
					temp = "('"+w1+"', '"+w2+"')"
					if w1 in line and w2 in line and w1 != w2:
						print w1+" "+w2
			

def main(argv):
	inputfile = ''
	outputfile = ''
	stmt1 = ''
	stmt2 = ''
	try :
		opts,args = getopt.getopt(argv, "hi:o:1:2:",["ifile=","ofile=","sent1=","sent2="])
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
		elif opt in ("-1","--sent1") :
			stmt1 = arg
		elif opt in ("-2","--sent2") :
			stmt2 = arg
	compute_bi_gram(inputfile,outputfile)
	compute_bi_gram_for_stmt(stmt1,outputfile)
	compute_bi_gram_for_stmt(stmt2,outputfile)

if __name__ == "__main__" :
	if len(sys.argv) == 0 :
		print 'Invalid number of options'
	else :
		main(sys.argv[1:])
