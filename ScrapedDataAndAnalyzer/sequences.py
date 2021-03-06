import random
import pprint

def seqStats(poolTotal, mainTotal):
    
    random.seed(0)
    trialCount = 0
    trials = []

    blocks = []
    for index in range(poolTotal):
        blocks.append(1)
    for index in range(poolTotal, mainTotal):
        blocks.append(0)
      
    for trial in range(1000):
    
        for index in range(len(blocks)-1, 0, -1):
            swapIndex = random.randint(0, 1000000000) % index
            holder = blocks[index]
            blocks[index] = blocks[swapIndex]
            blocks[swapIndex] = holder
            
        seqArray = []
        for i in range(11):
            seqArray.append(0)
        
        index = 0
        while index < len(blocks):
            seqSize = 0
            if blocks[index] == 1:
                seqSize += 1
                index += 1
                while index < len(blocks):
                    if blocks[index] == 1:
                        seqSize += 1
                        index += 1
                    else:
                        break
            
            if(seqSize < len(seqArray) and seqSize != 0):
                seqArray[seqSize] += 1
                
            index += 1
        
        trialCount += 1
        trials.append(seqArray)
    
    seqAvg = []
    for seqSize in range(11):
        total = 0
        for trial in trials:
            total += trial[seqSize]
        seqAvg.append(total / len(trials))
    
    stdDev = []
    for seqSize in range(11):
        total = 0
        for trial in trials:
            total += (trial[seqSize] - seqAvg[seqSize])**2
        stdDev.append((total/len(trials))**(1/2))
    
    stats = []
    stats.append(seqAvg)
    stats.append(stdDev)
        
    return stats

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

def theoryProbs(mainBlks, poolBlks):
    tProbs = []
    hPow = []
    
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
        pprint.pprint(oProbs[i])
        pprint.pprint(tProbs[i])
    
    obsSeqs = []
    seqStats = []
    
    for i in range(2):
        obsSeqs.append(seqs(poolBlks[i]))
        seqStats.append(seqStats(len(poolBlks[i]), len(mainBlks[i])))
        
    for i in range(len(obsSeqs)):
        pprint.pprint(obsSeqs[i])
        pprint.pprint(seqStats[i][0])
        pprint.pprint(seqStats[i][1])
    
main()