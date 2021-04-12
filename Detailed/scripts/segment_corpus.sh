########################################################################################################
#Script that segments a corpus using BPE and a range of merges                                         #
#												       #
#Input: - A folder with a set of text files, ideally one language per file
#       - Range of BPE merges we want to apply
#
#Output: An output folder that contains (for each text file) a .model and .freqs files
#         
#How to run: ./segment_corpus.sh
####################################################################################################

# Declare input corpus and range of merges:
input_corpus=corpusPBC #The input corpus folder with several text files (one per language). This must be a subfolder inside ../corpora/
declare -i init=350     #initial merge
declare -i final=5000   #final merge
declare -i step=50     #Step size

outputfolder=segmented_"$input_corpus"_"$init"_"$final"_"$step"  #The results will be stored in this folder (under ../output/)

rm -rf ../output/"$outputfolder"
mkdir ../output/
mkdir ../output/"$outputfolder"

for f in `ls ../corpora/"$input_corpus"/`; #For each language/file in the corpus folder

do	
	echo "Processing $f"
	mkdir ../output/"$outputfolder"/"$f"

	#For each merge:
	for ((i=init; i<=final; i=i+step)); 
	do
		#We learn the BPE model (lower case):
		tr '[:upper:]' '[:lower:]' < ../corpora/"$input_corpus"/"$f"| subword-nmt learn-bpe -s "$i" >../output/"$outputfolder"/"$f"/"$f"."$i".model
		
		#We apply it:
		tr '[:upper:]' '[:lower:]' < ../corpora/"$input_corpus"/"$f"|subword-nmt apply-bpe -c ../output/"$outputfolder"/"$f"/"$f"."$i".model > ../output/"$outputfolder"/"$f"/"$f"."$i".txt

		#We calculate frequencies of each segmented file:	
		python3 freq.py ../output/"$outputfolder"/"$f"/"$f"."$i".txt

		#We erase the segmented version of the corpus (*.txt) to free space. We only keep the model, and the frequency of the BPE segments:
		rm ../output/"$outputfolder"/"$f"/"$f"."$i".txt
		
		
	done
	
	
	
done

echo "DONE. See output in ../output/$outputfolder"

