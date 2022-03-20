# Filename: SubSumTests.py
# Author: Joshua Lollis
# Last Rev: 3/20/22
# This file contains the tests for subsum.py functions
#   Subset Summation
#   Candidate Generation
#   Candidate Verification
# This test file will import its dependencies on its own
# Just make sure that subsum.py is reachable from here.
from subsum import *
if __name__ == "__main__":
    def VerifierTest(inputs: list[int], candidate: list[int], target: int):
        """Test the Verifier portion of subsum in Isolation."""
        print("Inputs: {}".format(inputs))
        print("Candidate: {}".format(candidate))
        print("Target: {}".format(target))
        print("Verified: {}".format(Verifier(inputs, candidate, target)))

    testIn = [1,2,3,4,5]
    testCand = [2,3,5]
    testTarg = 10 #this is a success for 2+3+5
    VerifierTest(testIn, testCand, testTarg)

    def GeneratorTest(inputs: list[int]):
        """Test the Generator portion of subsum in Isolation"""
        for subset in GenerateCandidate(inputs):
            print(subset)
    testInput = [1,2,3,4,5,6,7,8,9,10]
    GeneratorTest(testInput)


    def SubsetSummationTest():
        """Test the Summation portion itself, of subsum in Isolation"""
        input = [1,6,8,2,4,9,12]
        targetK = 17    
        print("*Results*\n Input: {}\nSet: {}\nTarget: {}".format(input,SubsetSummation(input, targetK), targetK))
    SubsetSummationTest()
