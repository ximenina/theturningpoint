### Requirements:
* Python 3.X
* BPE  [subword-nmt](https://github.com/rsennrich/subword-nmt/).

In case you want to run the pipeline, go to `scripts/` and execute:

### 1. Segment a corpus and store subword frequencies at each incremental BPE merge:
`./segment_corpus.sh`

### 2. Calculate several measures (TTR, entropy, redundancy of subwords) over the segmented corpus at each merge:
`./apply_measures.sh`

(Before executing these scripts you must modify the *.sh files in order to set different parameters, i.e., corpus input folder, number of merges, etc.)

* Folder `output` contains the results. For instance, `output/MEASURES_corpusPBC_0_350_1` contains the measures obtained from merge 0 to merge 350 (Step size=1)
* Folder `corpora/corpusPBC` contains the pre-processed subset of the [PBC corpus](http://www.christianbentz.de/MLC2019/PBC49.zip) used for the experiments


