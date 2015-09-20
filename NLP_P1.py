#!/usr/bin/python

import sys, getopt

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

if __name__ == "__main__" :
	main(sys.argv[1:])
