def seqs(list):
    seqArray = [];
    for i in range(11):
        seqArray.append(0)
    
    index = 0;
    
    while index < len(list):

        count = 1
        current = list[index]
        
        if index+1<len(list):
            next = list[index+1]
            while next == current+1:
                count += 1
                if index+2 < len(list):
                    index += 1
                    current = list[index]
                    next = list[index+1]
                else:
                    break
                    
        seqArray[count] += 1
        index += 1
        
    return seqArray
    
def hashPow(mainBlks, poolBlks):
    hPow = []
    
    for i in range(len(mainBlks)):
        hPow.append(len(poolBlks[i])/len(mainBlks[i]))
    
    return hPow

def theoryProbs(mainBlks, poolBlks, hPow):
    tProbs = []
    
    for i in range(len(mainBlks)):
        hPow.append(len(poolBlks[i])/len(mainBlks[i]))
        
    for i in range(len(hPow)):
        tProbs.append([])
        for j in range(11):
            tProbs[i].append(hPow[i]**j)
        
    return tProbs

def obsProbs(mainBlks, poolBlks):
    
    oProbs = []
    
    for i in range(len(poolBlks)):
        seqVals = seqs(poolBlks[i])
        oProbs.append([])
        for j in range(len(seqVals)):
            oProbs[i].append(seqVals[j]/(len(mainBlks[i]) - 2))
    
    return oProbs
        
          
def main():
    
    poolBlks = [[1,2,3,5,7,8,10,13,18],[23,25,28,29,30,35,36,39]]
    mainBlks = [[1,2,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[21,22,23,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]]
    
    oProbs = obsProbs(mainBlks, poolBlks)
    tProbs = theoryProbs(mainBlks, poolBlks)
    
    for i in range(len(oProbs)):
        print(oProbs[i], tProbs[i])
    
main()