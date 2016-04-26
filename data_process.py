import csv
from collections import OrderedDict


def main():
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
        if len(i[0]) > 6:
                Antpool.remove(i)
        else:
            i[1] = (i[1].split(' ')[0])
            i[0] = int(i[0], 10)
            while len(i) > 2:
                i.pop(2)        
    
    cleanedBlks = []
    data.pop(0)
    for i in data:
        if len(i[0]) > 6 or i[0] == 'Height':
            data.remove(i)
        else:
            i[1] = (i[1].split(' ')[0])
            i[0] = int(i[0], 10)
            dates.append(i[1])
            while len(i) > 2:
                i.pop(2)
            cleanedBlks.append(i)
            
    blkDates = list(OrderedDict.fromkeys(dates))
    
    blkTotals = OrderedDict.fromkeys(dates)
    for i in blkDates:
        blkTotals[i] = 0
    
    for i in cleanedBlks:
        blkTotals[i[1]] += 1

    print(blkTotals)

		
main()