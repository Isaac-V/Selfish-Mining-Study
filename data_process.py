import csv
from collections import OrderedDict, Counter
import itertools
import pprint

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

    data = list(split_seq(data, 500))

    for i in data:
        F2Blks.append(sorted(list(set.intersection(set(i), set(F2pool)))))

    for i in data:
        AntBlks.append(sorted(list(set.intersection(set(i), set(Antpool)))))
    
    hPower = hashPow(data, AntBlks)
    
    tProbs = theoryProbs(data, AntBlks, hPower)
    
    oProbs = obsProbs(data, AntBlks)
    
    for i in range(len(oProbs)):
        print('#####################################')
        pprint.pprint(tProbs[i])
        pprint.pprint(oProbs[i])
        
     
main()