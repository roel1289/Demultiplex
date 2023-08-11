#!/usr/bin/ env python

# Author: Ross Ellwood roel@uoregon.edu

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.4"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = set('ATGCNatgcn')
RNA_bases = set('AUGCNaugcn')
DNA="ATCG"
RNA="AUCG"


def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    phred = ord(letter) #convert from phred score to number
    return (phred - 33) #subtract 33 bc illumina scores are offset by 33

def qual_score(phred_score: str) -> float:
    '''Write your own doc string'''
    sum: int= 0
    for phredScoreValues in phred_score:
        sum += convert_phred(phredScoreValues)    #sum of all variables
    return (sum / len(phred_score))               #sum of variables divided by number of values

def validate_base_seq(seq,RNAflag=False):
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    
    return set(seq)<=(RNA_bases if RNAflag else DNA_bases) #uses set




def gc_content(DNA):
    '''Calculating GC content and returning the GC content as a float between 0 and 1'''
    assert validate_base_seq(DNA)
    DNA=DNA.upper()
    DNAlength = len(DNA)
    GC=DNA.count("G") + DNA.count("C") #calculate Gs and Cs
    
    #non_GC=DNA.count("A") + DNA.count("T")
    return GC / len(DNA)     


def calc_median(testScores) -> int:
    """This function is taking the list of values and outputting the 
    mean for each nucleotide position. The values will be in 
    ascending order."""
    
    #determining odd or even lengths of the each line
    if len(testScores)%2 == 0: #even
        
        rightVal = (len(testScores))//2
        leftVal = rightVal -1
        medianValue = (testScores[rightVal]+testScores[leftVal])/2
        
        
    if len(testScores)%2 == 1: #odd
        midVal = (len(testScores))//2
        medianValue = testScores[midVal]
                 
    return medianValue


def oneline_fasta(read_file, write_file):
    with open(read_file, "r") as rf, open(write_file,"w") as wf:
        seq = ''
        while True:
            line = rf.readline().strip()
            if not line:
                break
            if line.startswith(">"):
                if seq != "":
                    wf.write(seq + "\n") 
                seq = ''
                wf.write(line + "\n") 
            else:
                seq += line 
        wf.write(seq)



#testing module with various assert tests
if __name__ == "__main__":
    assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    assert validate_base_seq("Hi there!") == False, "Validate base seq fails to recognize nonDNA"
    assert validate_base_seq("Hi there!", True) == False, "Validate base seq fails to recognize nonDNA"
    print("Passed DNA and RNA tests")
    
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATCGAT") == 0.5
    print("correctly calculated GC content")
    
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    assert calc_median ([0,1,2,3,4]) == 2
    assert calc_median([3,3,6,9,9,9]) == 15/2
    print("Calc median is working")

    assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    print("Passed DNA and RNA tests")