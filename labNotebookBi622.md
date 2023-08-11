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

Realized my open statement has to be in this format with gzip
```gzip.open(file, "rt") as ___```

Also realized that I had avg. loop commented out, so I am cancelling job and starting again
```$ scancel 23617```

Now ran it again with better argparse parameters, to take read length into account (101 or 8)
Located in ```/projects/bgmp/roel/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1SlurmScript.sh```

Ran again using the following 4 scripts (ran separate times for separate jobs):
```
/usr/bin/time -v ./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -l 101
/usr/bin/time -v ./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -l 8
/usr/bin/time -v ./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -l 8
/usr/bin/time -v ./part1PythonScript.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -l 101
```
Seemed to have worked and all exit statuses are 0


Now i am seeing how many index reads have "N"
```
zcat 1294_S1_L008_R2_001.fastq.gz | sed -n '2~4p' | grep "N" | wc -l
zcat 1294_S1_L008_R3_001.fastq.gz | sed -n '2~4p' | grep "N" | wc -l
```
lines for R2: 3976613
lines for R3: 3328051

Percentage of "N" R1:  3976613 / 363246735 = 0.010947415673261317
Percentage of "N" R2: 3328051 / 363246735 = 0.009161957092332846


Divide number of lines with "N" by total number of reads to get % of lines with "N"

### Part 3
Created python script (part3PythonScript.py) and was ran using bash script (part3DemuSlurm.sh).  
Results form slurm script:
```
 Command being timed: "./part3PythonScript.py -f1 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -f2 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -f3 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -f4 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"
        User time (seconds): 3267.72
        System time (seconds): 67.58
        Percent of CPU this job got: 69%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1:20:22
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 248444
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 37656
        Voluntary context switches: 58281
        Involuntary context switches: 3878
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
```
