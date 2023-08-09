#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=roel@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB

file1=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz
file2=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz
file3=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz
file4=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz


/usr/bin/time -v ./part3PythonScript.py -f1 $file1 -f2 $file2 -f3 $file3 -f4 $file4 