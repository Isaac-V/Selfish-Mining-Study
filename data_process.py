import csv
from collections import OrderedDict, Counter
import itertools
import pprint


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

    data = list(split_seq(data, 50))

    for i in data:
        F2Blks.append(sorted(list(set.intersection(set(i), set(F2pool)))))

    for i in data:
        AntBlks.append(sorted(list(set.intersection(set(i), set(Antpool)))))


    print 'Ant', AntBlks[0:4]
        
main()