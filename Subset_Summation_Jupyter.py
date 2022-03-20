# Author: Joshua Lollis
# Last Rev: 3/20/22
# This is a Jupyter notebook for the implementation and testing of the 
# Subset Summation problem as seen in HW6 7-5a.
# Simply follow the Headers attached to each cell below and it's pretty straightforward.

# %%
# 1) RUN THIS CELL TO DEFINE THE 3 METHODS FOR SUBSET SUMMATION PROBLEM
def SubsetSummation(inputs, target):
    for candidate in Candidate_Generator(inputs):
        if Verifier(inputs, candidate, target):
            return candidate
def Candidate_Generator(inputs):
    inInts = []
    for elem in inputs:
       inInts.append(elem)        
    for i in range(2 ** len(inInts)):
        S = []
        for j in range(len(inInts)):
            if ((i >> j) & 1) == 1:
                S.append(inInts[j])
        yield S
def Verifier(inputs, candidate, target):

    if(sum(candidate) == target):
        return True
    else:
        return False
##########################################################################


# %%
# 2) RUN THIS CELL (AFTER RUNNING [1]) TO TEST VERIFIER
def VerifierTest(inputs, candidate, target):
    print("Inputs: {}".format(inputs))
    print("Candidate: {}".format(candidate))
    print("Target: {}".format(target))
    print("Verified: {}".format(Verifier(inputs, candidate, target)))

testIn = [1,2,3,4,5]
testCand = [2,3,5]
testTarg = 10 #this is a success for 2+3+5
VerifierTest(testIn, testCand, testTarg)
########################################################################



# %% 
# 3) RUN THIS CELL (AFTER RUNNING [1]) TO TEST GENERATOR
def GeneratorTest(inputs):
    for subset in Candidate_Generator(inputs):
        print(subset)
testInput = [1,2,3,4,5,6,7,8,9,10]
GeneratorTest(testInput)
##########################################################################


#%%
# 4) RUN THIS CELL (AFTER RUNNING [1]) TO TEST THE ENTIRE SUBSET SUMMATION SOLUTION
def SubsetSummationTest():
    input = [1,6,8,2,4,9,12]
    targetK = 17    
    print("*Results*\n Input: {}\nSet: {}\nTarget: {}".format(input,SubsetSummation(input, targetK), targetK))
SubsetSummationTest()
##########################################################################


