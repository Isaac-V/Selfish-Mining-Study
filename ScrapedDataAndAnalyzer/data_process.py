from __future__ import division
import csv
from collections import OrderedDict, Counter
import itertools
import pprint
import random

seqMax = 11
f1 = open('BigDeviations.csv', 'w') 

def seqSims(pool, poolBlks, mainBlks):
    
    poolTotal = len(poolBlks)
    mainTotal = len(mainBlks)
    
    random.seed(0)
    rows = []
    
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
        for i in range(seqMax):
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
            
        for index in range(1, len(seqArray)):
            rows.append(str(trial) + ',' + str(index) + ',' + str(seqArray[index]))

        trials.append(seqArray)
    
    seqAvg = []
    for seqSize in range(seqMax):
        total = 0
        for trial in trials:
            total += trial[seqSize]
        seqAvg.append(total / len(trials))
    
    stdDev = []
    for seqSize in range(seqMax):
        total = 0
        for trial in trials:
            total += (trial[seqSize] - seqAvg[seqSize])**2
        stdDev.append((total/len(trials))**(1/2))
        
    bigDevs = []
    obsSeqs = seqs(poolBlks)
    for index in range(1, len(obsSeqs)): 
        if stdDev[index] > 0:
            deviations = abs(obsSeqs[index] - seqAvg[index]) / stdDev[index]
            if deviations > 2:
                devStr = pool + ',' + str(mainBlks[0]) + ',' + str(mainBlks[mainTotal - 1]) + ','
                devStr += str(index) + ',' + str(obsSeqs[index]) + ',' + str(seqAvg[index]) + ','
                devStr += str(stdDev[index]) + ',' + str(deviations)
                bigDevs.append(devStr)

    for line in bigDevs:
        f1.write(line + '\n')
        
    return rows
    
    
def seqs(list):

    seqArray = []
    for i in range(seqMax):
        seqArray.append(0)
    
    index = 0
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
        
    for i in range(len(hPow)):
        tProbs.append([])
        for j in range(seqMax):
            tProbs[i].append(hPow[i]**j)
        
    return tProbs

def obsProbs(mainBlks, poolBlks):
    
    oProbs = []
    
    for i in range(len(poolBlks)):
        seqVals = seqs(poolBlks[i])
        oProbs.append([])
        for j in range(len(seqVals)):
            oProbs[i].append(seqVals[j]/(len(mainBlks[i]) - (j-1)))
    
    return oProbs


def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))


def main():
    prev_line = []
    seq = []
    Antpool = []
    AntpoolTotal = []
    F2pool = []
    data = []
    dates = []
    totals = []
    with open('blockchain.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)


    with open('AntPoolBlockData.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            Antpool.append(row)

    with open('F2PoolBlockData.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            F2pool.append(row)
    F2pool.pop(0)
    for i in F2pool:
        i[0] = int(i[0], 10)
    F2pool.reverse()




    Antpool.pop(0)
    for i in Antpool:

        while len(i) > 1:
            i.pop(1)
        i[0] = int(i[0], 10)
            
        


    data.pop(0)
    for i in data[:]:
        while len(i) > 1:
            i.pop(1)
        if len(i[0]) > 6:
            data.remove(i)

    for i in data:
        i[0] = int(i[0], 10)
    data.reverse()

    F2Blks = []
    AntBlks = []
    F2pool = list(itertools.chain.from_iterable(F2pool))
    data = list(itertools.chain.from_iterable(data))
    Antpool = list(itertools.chain.from_iterable(Antpool)) 
    
    splitSize = 100
    
    data = list(split_seq(data, splitSize))

    for i in data:
        F2Blks.append(sorted(list(set.intersection(set(i), set(F2pool)))))

    for i in data:
        AntBlks.append(sorted(list(set.intersection(set(i), set(Antpool)))))
    
#    hPower = hashPow(data, F2Blks)
#    tProbs = theoryProbs(data, F2Blks, hPower)
#    oProbs = obsProbs(data, F2Blks)    
#    f = open('resultsF2.csv', 'w')  
#    for i in range(11):
#        currRow = ''
#        for j in range(len(tProbs)):
#            currRow += str(tProbs[j][i]) + ',' + str(oProbs[j][i]) + ','
#        f.write(currRow + '\n')

    header = 'pool,startHeight,endHeight,type,trial,seqLength,count'
    
    statRows = []
    statRows.append(header)
    
     
    f1.write('pool,startHeight,endHeight,seqLength,observed,expected,stdDev,deviations' + '\n')
    
    for index in range(len(data)):
        print('Blocks Processed ~ ' + str(splitSize*index))
        startHeight = str(data[index][0])
        endHeight = str(data[index][len(data[index])-1])
        antPrefix = 'AntPool,' + startHeight + ',' + endHeight + ','
        f2Prefix = 'F2Pool,' + startHeight + ',' + endHeight + ','
        
        antObs = seqs(AntBlks[index])
        for seqLen in range(1, len(antObs)):
            obsRow = '-1' + ',' + str(index) + ',' + str(antObs[seqLen])
            statRows.append(antPrefix + 'Observed,' + obsRow)
        
        antSims = seqSims('AntPool', AntBlks[index], data[index])
        for row in antSims:
            statRows.append(antPrefix + 'Simulated,' + row)
        
        f2Obs = seqs(F2Blks[index])
        for seqLen in range(1, len(f2Obs)):
            obsRow = '-1' + ',' + str(index) + ',' + str(f2Obs[seqLen])
            statRows.append(f2Prefix + 'Observed,' + obsRow)
        
        f2Sims = seqSims('F2Pool', F2Blks[index], data[index])
        for row in f2Sims:
            statRows.append(f2Prefix + 'Simulated,' + row)
            
    f2 = open('results' + str(splitSize) + '.csv', 'w')  
    for row in statRows:
        f2.write(row + '\n')
    
main()