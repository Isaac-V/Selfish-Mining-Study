import csv
from collections import OrderedDict


def main():
	data = []
	dates = []
	totals = []
	with open('blockchain.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        data.append(row)
	data.pop(0)
	for i in data:
		i.pop(2)
		i.pop(2)
		i[1] = (i[1].split(' ')[0])
		dates.append(i[1])
	
	temp = list(OrderedDict.fromkeys(dates))

	print len(temp)


		
main()