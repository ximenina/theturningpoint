#################################################################################
#Script for calculating frequencies of types for a given file                   #
#input: Text file                                                               #
#Output: .freqs.tsv file        			                                #
#################################################################################

import os
import sys
from re import sub
import numpy as np
from collections import defaultdict, Counter
import re
import string 


inputcorpus=sys.argv[1]
myfile=open(inputcorpus,'r', encoding="utf-8")
output=inputcorpus+".freqs.tsv"
outputfile=open(output,'w', encoding="utf-8")
strings=myfile.read().lower().split() #we normalize lower case, strip blank spaces at the beginning end.
punctuation=["!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","}","~","]","¿","»","«","“","”","¡","،"] #Specific punctuation marks that we don0t want to take into account.


#Removing punctuation:
file_clean=[]
for s in strings:
	#print(s) 
	#if it's only one symbol, and that symbols is a puntuation mark
	if (len(s) == 1): 
		if (s in punctuation):
			continue    #we don't add this to the array
		

	file_clean.append(s) 

frequency=Counter(file_clean)

#We print Frequencies:
for value, key in sorted([(j,i) for i,j in frequency.items()], reverse=True):
	if (key != ""):
		outputfile.write(str(key)+ '\t'+str(value)+'\n')
		#print (str(key)+ '\t'+str(value)+'\n')

myfile.close()
outputfile.close()
