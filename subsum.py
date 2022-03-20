# Filename: subsum.py
# Author: Joshua Lollis
# Last Rev: 3/20/22
# This is the "Solution" for the Subset Summation "Problem" from ADITA Exercise 7-5a
# Import this module to your own environment to make use of:
#   Subset Summation
#   Candidate Generation
#   Candidate Verification

def SubsetSummation(inputs: list[int], target: int):
    """Return a subset in which the sum of it's elements is equal to the target 
        (or) 
       Return [None] if no such subset exists."""
    for candidate in GenerateCandidate(inputs):
        if Verifier(inputs, candidate, target):
            return candidate
    return None
##########################################################################

def GenerateCandidate(inputs: list[int]):
    """Generator Function yielding each subset of inputs list"""
    inInts = []
    for elem in inputs:
       inInts.append(elem)        
    for i in range(2 ** len(inInts)):
        S = []
        for j in range(len(inInts)):
            if ((i >> j) & 1) == 1:
                S.append(inInts[j])
        yield S
##########################################################################

def Verifier(inputs: list[int], candidate: list[int], target: int):
    """Return True if sum of candidate elements = target integer
        (or)
       Return False"""
    if(sum(candidate) == target):
        return True
    else:
        return False
