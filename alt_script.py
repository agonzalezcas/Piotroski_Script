import csv
import sys
import numpy as np
# datafile = open(sys.argv[1],'r')
datafile = open("2005.csv",'r')
datareader = csv.reader(datafile, delimiter =",")
data = list(datareader)
del data[0:4]
# tran_data = map(list,zip(*data))
for i in xrange(0,len(data)):
	for j in xrange(2,len(data[i])):
		try:
			data[i][j] = float(data[i][j])
		except:
			data[i][j] = 0.0
# tran_data = map(list,zip(*data))
dictionary = {row[1]:row[0:1]+row[2:] for row in data}
for index in dictionary:
	print index,dictionary[index]
	print "\n"