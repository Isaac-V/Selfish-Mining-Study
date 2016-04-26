import csv
from collections import OrderedDict, Counter


def main():
	Antpool = []
	F2pool = []
	data = []
	dates = []
	totals = []
	with open('blockchain.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        data.append(row)


	with open('AntPoolBlockData.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        Antpool.append(row)

	with open('F2PoolBlockData.csv', 'rb') as f:
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
	print 'SUM', sum(temp.values())
	temp = temp.items()

	for word in temp:
		print word



	

		
main()