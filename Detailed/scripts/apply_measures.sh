########################################################################################################
#Script that calculates types, tokens, H and R for each merge and for each language.
#Input:	A BPE segmented corpus (segmented_ folder obtained from running ./segment_corpus.sh)
#Output: A folder ../output/MEASURES_ that contains for each segmented text: Types, Tokes, TTR, H, R; Plots; and a Summary of max/min per each language
#
#How to run: apply_measures.sh
####################################################################################################


# Declare input corpus folder, segmented corpus folder and range of merges:
input_corpus=corpusPBC #The input corpus folder with several text files (one per language). This must be a subfolder inside ../corpora/
segmented_corpus=segmented_corpusPBC_0_350_1   #The folder that contains the segmented version of the input corpus, must be inside ../output/
declare -i init=0     #initial merge
declare -i final=350   #final merge
declare -i step=1     #Step size


outputfolder=MEASURES_"$input_corpus"_"$init"_"$final"_"$step" #The results will be stored in this folder (under ../output/)

rm -rf ../output/"$outputfolder"
mkdir ../output/"$outputfolder"
mkdir ../output/"$outputfolder"/measures
mkdir ../output/"$outputfolder"/plots


#creating files and headers for the summaries:
echo "file	merge_min	min_ttr	merge_max	max_ttr	initial_ttr	final_ttr"> ttr.summary.tsv
echo "file	merge_min	min_entropy	merge_max	max_entropy	initial_entropy	final_entropy"> entropy.summary.tsv
echo "file	merge_min	min_redundancy	merge_max	max_redundancy	initial_redundancy	final_redundancy"> redundancy.summary.tsv


for f in `ls ../corpora/"$input_corpus"/`; #For each language/file in the corpus folder

do	
	echo "Processing $f"
	
	#preparing the file that will store the entropy/TTR values for each merge (one for each language):
	echo "file	merge	types	tokens	TTR	entropy	redundancy">../output/"$outputfolder"/measures/"$f".measures.tsv
	
	for ((i=init; i<=final; i=i+step));
	do
		
		echo -n "$f	" >> ../output/"$outputfolder"/measures/"$f".measures.tsv				
		echo -n "$i	" >> ../output/"$outputfolder"/measures/"$f".measures.tsv # -n indicates not to break line after this echo
		#Calculating the measures taking just the requency list on files *.freqs.tsv
		python3 measures_fromlist.py ../output/"$segmented_corpus"/"$f"/"$f"."$i".txt.freqs.tsv >> ../output/"$outputfolder"/measures/"$f".measures.tsv 
		
	done

	#Now that we have the measures for a language, we process them in order to extract a summary and plots:
	python3 summary_plot.py ../output/"$outputfolder"/measures/"$f".measures.tsv
	

	#moving plots (and renaming them to be shorter):
	mv "$f".measures.tsv_ttr.png ../output/"$outputfolder"/plots/"$f".ttr.png
	mv "$f".measures.tsv_redundancy.png ../output/"$outputfolder"/plots/"$f".redundancy.png
	mv "$f".measures.tsv_entropy.png ../output/"$outputfolder"/plots/"$f".entropy.png
	
	
done
#Moving summaries:
mv *.summary.tsv ../output/"$outputfolder"/


echo "DONE. See output in ../output/$outputfolder"

