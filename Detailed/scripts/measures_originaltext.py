##Script for calculating unigram entropy, space separated words
#####

from __future__ import division
from collections import defaultdict, Counter
from itertools import chain
from re import escape, compile
#import matplotlib.pyplot as plt
import numpy as np
import sys
from re import sub


inputcorpus=sys.argv[1]
myfile=open(inputcorpus,'r', encoding="utf-8")
strings=myfile.read().lower().split()

punctuation=["!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","}","~","]","¿","»","«","“","”","¡","،"]


strings_clean=[]

#removing punkt, just in cases there is no @@:
for s in strings:
	#print(s) 
	#if it's only one symbol, and that symbols is a puntuation mark
	if (len(s) == 1): 
		if (s in punctuation):
			continue    #we don't add this to the array
		

	strings_clean.append(s) 

#strings_clean = [sub(r'[^\w\s]','',w) for w in strings] 
words = Counter(strings_clean)

types=len(set(strings_clean))
tokens=len(strings_clean)
ttr=types/tokens


def get_measures(voc):
	freq = defaultdict(int)
	for key, value in words.items():
		if (key != ""):
			freq[key] += value
	#print(freq)
	freq = np.array(list(freq.values()))
	#Probabilidad de los símbolos
	p = freq/freq.sum()
	#print (p)
	len_p=len(p)

	Hcross = (-(1./len_p)*np.log2(p)).sum()  #cross-entropy
	H=-(p*np.log2(p)).sum()  #entropy
	R=1-(H/np.log2(len_p)) #redundancy

	return  H,Hcross,R



results=get_measures(words)

print(str(types)+"\t"+str(tokens)+"\t"+str(ttr)+"\t"+str(results[0])+"\t"+str(results[1])+"\t"+str(results[2]))  #Print entropy
