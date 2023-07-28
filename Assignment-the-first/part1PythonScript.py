#!/usr/bin/env python

#import things:
import argparse
import bioinfo
import gzip 



def get_args():
    parser = argparse.ArgumentParser(description="A program to hold input + output file name")
    parser.add_argument("-f", "--filename", help="Specify the input filename.", type = str)
    parser.add_argument("-o", "--output", help="Specify output filename.", type = str)
    return parser.parse_args()

args = get_args()
file = args.filename

#making function to create list of 101 values (0.0)
def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    
    i = 0                               #start counter at 0
    while i < 101:                      #while it is true that i is less than 101
    
        lst.append(value)               #append the value(0.0) to list
        i+=1                            #continue incrementing the list (and will stop at 100)
    return lst

#ititialize my_list to have 101 zeros (floats)
my_list: int = []
my_list = init_list(my_list)

#populating the list
def populate_list(file: str) -> tuple[list, int]:
    """Creating a list of the sum of quality scores. The list is 101 values long and each mean
    is created using each of the reads."""
    num_lines = 0

#read in file and create out file
    with gzip.open(file,"r") as fastqFile:                  #, open(args.output, "w") as out_file:
        i = 0   #counter called "count" that tracks number of lines in file
        for line in fastqFile:
            num_lines += 1

            i += 1
            line = line.strip('\n')
            
            if i%4 == 0:
                for qual in range(len(line)):
                    my_list[qual] += bioinfo.convert_phred(line[qual])               

    return my_list, num_lines

my_list, num_lines = populate_list(file)

# print(f'Base Pair\tMean Quality Score')

# for base in range(len(my_list)):
#     my_list[base] = my_list[base] / (num_lines/4)
    
#     print(f'{base}\t{my_list[base]}')


import matplotlib.pyplot as plt

plt.bar(range(len(my_list)), my_list )
plt.xlabel('Nucleotide')
plt.ylabel('Mean Quality Score')
plt.title('Mean Quality Score for each Nucleotide location')
plt.savefig("outputHist.png")
plt.show()

#test: ./part1PythonScript.py -f ../TEST-input_FASTQ/R1test.fq -o OUTtest.txt