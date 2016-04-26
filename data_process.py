import csv
from collections import OrderedDict, Counter


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

    Antpool.pop(0)
    for i in Antpool:
        i.pop(2)
        i.pop(2)
        i.pop(2)
        i.pop(2)
        if len(i) == 3:
            i.pop(2)
        i[1] = (i[1].split(' ')[0])
        antDate = i[1][1:]+'/'+i[1][:4]
        AntpoolTotal.append(andDate.replace('-','/'))


    data.pop(0)
    for i in data:
        i.pop(2)
        i.pop(2)
        i[1] = (i[1].split(' ')[0])
        dates.append(i[1])
    

    antMap = OrderedDict.fromkeys(AntpoolTotal)

    for i in AntpoolTotal:
        antMap[i] = []

    for i in Antpool:
        antMap[i[1]].append(i[0])
      
    dateMap = OrderedDict.fromkeys(dates)
    print dateMap

        
main()