########################################################################################################
#Script for simply calculating unigram word entropy TTR, Hrcross, redundancy of a text (each word separated by space)
####################################################################################################

input_corpus=corpusPBC_randomized
echo "file	types	tokens	TTR	H	Hcross	R">../OtherAnalyses/"$input_corpus".stats.txt

for f in `ls ../originalcorpora/"$input_corpus"/`;
do
	echo "Processing $f"	
	
	echo -n "$f	">>../OtherAnalyses/"$input_corpus".stats.txt
	python3 measures_originaltext.py ../originalcorpora/$input_corpus/"$f" >>../OtherAnalyses/"$input_corpus".stats.txt
		
done

echo "DONE. See ../OtherAnalyses/$input_corpus.stats.txt"

