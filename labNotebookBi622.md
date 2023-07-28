##### Lab notebook for Bi622. 
# Notes from 7/27/23
# part 1
which files contain which type of data in ```/projects/bgmp/shared/2017_sequencing``` :
```zcat 1294_S1_L008_R1_001.fastq.gz | head -n2 ```
Obvious that this is a biological read file
```zcat 1294_S1_L008_R2_001.fastq.gz | head -n2```
This file has the indexes for read 1
Using the same methods as above, I can tell that r1 = read1, r2 = index1, r3 = index2, and r4 = read2


##########
read length 
```zcat 1294_S1_L008_R1_001.fastq.gz | head -n2 | tail -n1 | wc -L```



Using conda environment:
``` conda activate bgmp-matplotlib```
interactive node:
```srun --account=bgmp --partition=compute --time=2:00:00 --pty bash```

Will try and use:
```./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz```

Decided to make bash script to sbatch the python script with argparse:
```
#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=roel@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=4                 #optional: number of cpus, default is 1
#SBATCH --mem=16GB                        #optional: amount of memory, default is 4GB

/usr/bin/time -v ./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz

```

```squeue -u roel``` # to see progress

Output: ```slurm-23565.out```
```
Passed DNA and RNA tests
correctly calculated GC content
Median value function inbound!
Your convert_phred function is working! Nice job
Traceback (most recent call last):
  File "/gpfs/projects/bgmp/roel/bioinfo/Bi622/Demultiplex/Assignment-the-first/./part1PythonScript.py", line 57, in <module>
    my_list, num_lines = populate_list(file)
                         ^^^^^^^^^^^^^^^^^^^
  File "/gpfs/projects/bgmp/roel/bioinfo/Bi622/Demultiplex/Assignment-the-first/./part1PythonScript.py", line 49, in populate_list
    line = line.strip('\n')
           ^^^^^^^^^^^^^^^^
TypeError: a bytes-like object is required, not 'str'
Command exited with non-zero status 1
        Command being timed: "./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
        User time (seconds): 0.03
        ...
        Exit status: 1
```
