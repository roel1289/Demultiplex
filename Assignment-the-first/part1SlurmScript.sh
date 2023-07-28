#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=roel@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=16GB                        #optional: amount of memory, default is 4GB

/usr/bin/time -v ./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -l 101 -o R1outHist.png

#/usr/bin/time -v ./part1PythonScript.py -f ../TEST-input_FASTQ/R1test.fq -o OUTtest.txt


#NOTE: change -f and -l each run. Read files will have -l 101 and index files will have -l 8