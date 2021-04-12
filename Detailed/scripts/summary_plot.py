#################################################################################################################
#Script that takes as an input a file that contains lines with the following measures (*.measures.tsv): 
#File	merge	types	tokens	TTR	H	R
#it returns a Summary with  statistics and a plot for each different measure
########################################################################################################################


from __future__ import division
from collections import defaultdict, Counter
from itertools import chain
from re import escape, compile
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import warnings
warnings.simplefilter("ignore")


inputcorpus=sys.argv[1]
myfile=open(inputcorpus,'r', encoding="utf-8")
info = list(csv.reader(myfile, delimiter='\t'))



merges = np.zeros(len(info))
entropies = np.zeros(len(info))
ttrs = np.zeros(len(info))
crossentropies = np.zeros(len(info))
rs = np.zeros(len(info))

fileparts=inputcorpus.split("/")
outputplot1=fileparts[-1]+"_ttr.png"
outputplot2=fileparts[-1]+"_entropy.png"
outputplot3=fileparts[-1]+"_redundancy.png"
#outputplot4=fileparts[-1]+"_combined1.png"
#outputplot5=fileparts[-1]+"_combined2.png"

label1="ttr"
label2="entropy"
label3="redundancy"


for j in range(1, len(info)):
	merges[j-1]=info[j][1]
	ttrs[j-1]=info[j][4]
	entropies[j-1]=info[j][5]
	rs[j-1]=info[j][6]



#remove last element from the array because is empty:
merges=merges[:-1]
entropies=entropies[:-1]
ttrs=ttrs[:-1]
rs=rs[:-1]

def min_max(values):
	minimum=min(values)
	maximum=max(values)
	merge_minimum=list(values).index(min(values)) # returns just the index (the lowest merge in case of more than one minimum)
	merge_maximum=list(values).index(max(values)) # returns just the index   (the lowest merge in case of more than one minimum)
	merge_minimum=merges[merge_minimum]
	merge_maximum=merges[merge_maximum]
	initial=values[0] 
	final=values[len(info)-2]

	return minimum, maximum, merge_minimum, merge_maximum, initial, final

results_entropies=min_max(entropies)
results_ttrs=min_max(ttrs)
results_rs=min_max(rs)

#Writting a summary per each measure:
output1="ttr.summary.tsv"
output2="entropy.summary.tsv"
output3="redundancy.summary.tsv"


output_ttr=open(output1,'a+', encoding="utf-8")
output_entropy=open(output2,'a+', encoding="utf-8")
output_r=open(output3,'a+', encoding="utf-8")


#output_ttr.write("file\tmerge_min\tmin_ttr\tmerge_max\tmax_ttr\tinitial_ttr\tfinal_ttr\n")
output_ttr.write(str(fileparts[-1])+'\t'+str(results_ttrs[2])+'\t'+str(results_ttrs[0])+'\t'+str(results_ttrs[3])+'\t'+str(results_ttrs[1])+'\t'+str(results_ttrs[4])+'\t'+str(results_ttrs[5])+'\n')

#output_entropy.write("file\tmerge_min\tmin_entropy\tmerge_max\tmax_entropy\tinitial_entropy\tfinal_entropy\n")
output_entropy.write(str(fileparts[-1])+'\t'+str(results_entropies[2])+'\t'+str(results_entropies[0])+'\t'+str(results_entropies[3])+'\t'+str(results_entropies[1])+'\t'+str(results_entropies[4])+'\t'+str(results_entropies[5])+'\n')

#output_r.write("file\tmerge_min\tmin_redundancy\tmerge_max\tmax_redundancy\tinitial_redundancy\tfinal_redundancy\n")
output_r.write(str(fileparts[-1])+'\t'+str(results_rs[2])+'\t'+str(results_rs[0])+'\t'+str(results_rs[3])+'\t'+str(results_rs[1])+'\t'+str(results_rs[4])+'\t'+str(results_rs[5])+'\n')


#Visualization:
plt.plot(merges, ttrs,'-v')
plt.xlabel('merge')
plt.ylabel(label1)
plt.title(inputcorpus)
plt.savefig(outputplot1)

plt.figure() 
plt.plot(merges, entropies,'-v')
plt.xlabel('merge')
plt.ylabel(label2)
plt.title(inputcorpus)
plt.savefig(outputplot2)


plt.figure()
plt.plot(merges, rs,'-v')
plt.xlabel('merge')
plt.ylabel(label3)
plt.title(inputcorpus)
plt.savefig(outputplot3)

#Combined Graphs:
#plt.figure() #a new figure withput overlapping previous dataset graph
#plot1, = plt.plot(merges, entropies,'-v')
#plot2, = plt.plot(merges, rs, '-v')
#plot3, = plt.plot(merges, ttrs, '-v')
#plt.xlabel('merge')
#plt.legend([plot1,plot2,plot3],["entropy","redundancy", "TTR"])
#plt.title(inputcorpus)
#plt.savefig(outputplot5)

