#!/usr/bin/env python

#import things:
import argparse
import bioinfo
import gzip 
#import numpy



def get_args():
    parser = argparse.ArgumentParser(description="A program to hold input + output file name")
    parser.add_argument("-f1", "--filename1", help="Specify the input filename.", type = str)
    parser.add_argument("-f2", "--filename2", help="Specify the input filename.", type = str)
    parser.add_argument("-f3", "--filename3", help="Specify the input filename.", type = str)
    parser.add_argument("-f4", "--filename4", help="Specify the input filename.", type = str)
    parser.add_argument("-o", "--output", help="Specify output filename.", type = str)
    return parser.parse_args()

args = get_args()
# file = args.filename


###Beginning of func to return rev comp of DNA strand
#key = forward strand nucl
#value = rev complement nucl
my_dict = {"A":"T","T":"A","G":"C","C":"G", "N":"N"}
def rev_comp_DNA(DNA:str) -> str:
    '''This function takes a string of A,G,C,T, and N and returns its reverse compliment.'''
    new_seq = ""
    
    for base in DNA:
        new_seq += my_dict[base]
    return(new_seq[::-1])

rev_comp_DNA("ANTTGNGNG")


#setting up way to read lines and strip
def readfour(fh):
    '''Sequence to run through file four lines at a time. Returns tuple-- each record is its own tuple.'''
    header=fh.readline().strip()
    seq=fh.readline().strip()
    plus=fh.readline().strip()
    qual=fh.readline().strip()

    return header, seq, plus, qual

#known indexes
#dictiionary includes indexes and the value is the occurences
#for the beginning, we are initializing the occurences to 0
knownDict = dict()
knownDict = {"GTAGCGTA":0,"AACAGCGA":0,"CTCTGGAT":0,"CACTTCAC":0,"CGATCGAT":0,"GATCAAGG":0,"TAGCCATG":0,"CGGTAATC":0,"TACCGGAT":0,"CTAGCTCA":0,"GCTACTCT":0,"ACGATCAG":0,"TATGGCAC":0,"TGTTCCGT":0,"GTCCTAAG":0,"TCGACAAG":0,"TCTTCGAC":0,"ATCATGCG":0,"ATCGTGGT":0,"TCGAGAGT":0,"TCGGATTC":0,"GATCTTGC":0,"AGAGTCCA":0,"AGGATAGC":0}

#unknown dictionary
unknownDict = dict()

#initialize matched, hopped and unknown dictionaries
instancesDict = dict()
instancesDict = {"matched":0, "hopped":0, "unknown":0}



#opening files
with open(args.filename1, "r") as R1, open(args.filename2, "r") as R2, open(args.filename3, "r") as R3, open(args.filename4, "r") as R4:
    while True: 
        record_r1=readfour(R1)
        if record_r1 == ("","","",""):
            break #break when there is an empty tuple
        record_r2=readfour(R2)
        record_r3=readfour(R3)
        record_r4=readfour(R4)
        reverse_index=rev_comp_DNA(record_r3[1])
        #print(reverse_index)
        new_header =" "+record_r1[0]+" "+record_r2[1]+"-"+reverse_index
        print(new_header)









#TEST: ./part3PythonScript.py -f1 ../TEST-input_FASTQ/R1test.fq -f2 ../TEST-input_FASTQ/R2test.fq -f3 ../TEST-input_FASTQ/R3test.fq -f4 ../TEST-input_FASTQ/R4test.fq 