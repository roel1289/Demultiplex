#!/usr/bin/ env python

# Author: Ross Ellwood roel@uoregon.edu

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.3"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = None
RNA_bases = None

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    pass
    phred = ord(letter) #convert from phred score to number
    return (phred - 33) #subtract 33 bc illumina scores are offset by 33

def qual_score(phred_score: str) -> float:
    '''Write your own doc string'''
    sum: int= 0
    for phredScoreValues in phred_score:
        sum += convert_phred(phredScoreValues)    #sum of all variables
    return (sum / len(phred_score))               #sum of variables divided by number of values

DNAbases = set('ATGCNatcgn')
RNAbases = set('AUGCNaucgn')



def validate_base_seq(seq: str, RNAflag: bool=False) -> bool:
    seq = seq.upper()
    return len(seq) == seq.count("A") + seq.count("U" if RNAflag else "T") + seq.count("G") + seq.count("C")

assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
print("Passed DNA and RNA tests")

def gc_content(DNA):
    '''Calculating GC content and returning the GC content as a float between 0 and 1'''
    
    DNA=DNA.upper()
    
    GC=DNA.count("G") + DNA.count("C") #calculate Gs and Cs
    
    #non_GC=DNA.count("A") + DNA.count("T")
    return GC / len(DNA)     

assert gc_content("GCGCGC") == 1
assert gc_content("AATTATA") == 0
assert gc_content("GCATCGAT") == 0.5
print("correctly calculated GC content")

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
print("Median value function inbound!")


def oneline_fasta():
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

    if __name__ == "__main__":
        pass
    # write tests for functions above, Leslie has already populated some tests for convert_phred
assert convert_phred("I") == 40, "wrong phred score for 'I'"
assert convert_phred("C") == 34, "wrong phred score for 'C'"
assert convert_phred("2") == 17, "wrong phred score for '2'"
assert convert_phred("@") == 31, "wrong phred score for '@'"
assert convert_phred("$") == 3, "wrong phred score for '$'"
print("Your convert_phred function is working! Nice job")



