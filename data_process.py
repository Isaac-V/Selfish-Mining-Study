import csv
from collections import OrderedDict, Counter


def main():
    prev_line = []
    seq = []
    Antpool = []
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

    Antpool.pop(0)
    for i in Antpool:
        i.pop(2)
        i.pop(2)
        i.pop(2)
        i.pop(2)
        if len(i) == 3:
            i.pop(2)
        i[0] = int(i[0], 10)
        i[1] = (i[1].split(' ')[0])

    data.pop(0)
    for i in data:
        i.pop(2)
        i.pop(2)
        i[1] = (i[1].split(' ')[0])
        dates.append(i[1])
    
    temp = Counter(dates)
    print('SUM', sum(temp.values()))
    temp = temp.items()

    for word in temp:
        print(word)
      
    dateMap = OrderedDict.fromkeys(dates)
    for i in dates:
        dateMap[i] = []
        
    for i in data:
        dateMap[i[1]].append(i[0])
    
    for i in dates:
        print(i,len(datemap[i]))
    
      
    print(temp)

    # for line in Antpool:
    #     if len(prev_line) > 0:
    #         print 'PREV LINE', prev_line
    #     prev_line = line


        
main()