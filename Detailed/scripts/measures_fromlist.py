####################################################################################################
#Script for calculating entropy, TTR, Redundancy					           #
#												   #
#Input: It receives a list of frequencies after BPE segmentation (*.freqs)			   #
####################################################################################################

from __future__ import division
from collections import defaultdict, Counter
from itertools import chain
from re import escape, compile
#import matplotlib.pyplot as plt
import numpy as np
import sys
from re import sub
import csv

def get_measures(voc):  #Returns H and R
	freq = defaultdict(int)
	for key, value in words.items():
		if (key != ""):
			freq[key] += value
	freq = np.array(list(freq.values()))
	#Probability of the symbols:
	p = freq/freq.sum()
	len_p=len(p)

	H=-(p*np.log2(p)).sum()  #entropy
	R=1-(H/np.log2(len_p)) #redundancy

	return  H,R


##We read the input:
inputcorpus=sys.argv[1]
myfile=open(inputcorpus,'r', encoding="utf-8")

with myfile as file_in:
	rows = []
	for row in file_in:
		if (not '"' in row):
        		rows.append(row)  #csv library is buggy, cannot deal with this: ", so we have to erase those lines

entries = list(csv.reader(rows, delimiter='\t'))  #Example: "ra@@	855"

words={}
for lines in entries:
	
	words[lines[0]]= int(lines[1])  

	
 #Types, tokens and TTR:  	
types=len(words)
tokens=sum(words.values())
ttr=types/tokens


#H and R:	
results=get_measures(words)

print(str(types)+"\t"+str(tokens)+"\t"+str(ttr)+"\t"+str(results[0])+"\t"+str(results[1]))  #Print MEASURES

