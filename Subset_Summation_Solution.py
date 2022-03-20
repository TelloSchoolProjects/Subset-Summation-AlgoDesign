
def SubsetSummation(inputs, target):
    for candidate in Candidate_Generator(inputs):
        if Verifier(inputs, candidate, target):
            return candidate
##########################################################################

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
##########################################################################

def Verifier(inputs, candidate, target):

    if(sum(candidate) == target):
        return True
    else:
        return False
