import csv 
import sys
# import numpy

# a = numpy.loadtxt(sys.argv[1], delimiter=',')
# if 'A B B India Ltd.' in a[:0]:
# 	print 'found'

#reading the first file
name=[]
symbol=[]
ti=[]
sales=[]
iffs=[]
eoi=[]
te=[]
cogs=[]
pat=[]
borow=[]
curr_lia=[]
tot_assets=[]
curr_assets=[]
net_cash_flow=[]
pb=[]
price=[]
with open(sys.argv[1]) as f:
	lines = f.readlines()

neglect=0
for line in lines:
	neglect+=1
	row=line.split(',')
	if(neglect>4):
		name.append(row[0])
		symbol.append(row[1])
		ti.append(row[2])
		sales.append(row[3])
		iffs.append(row[4])
		eoi.append(row[5])
		te.append(row[6])
		cogs.append(row[7])
		pat.append(row[8])
		borow.append(row[9])
		curr_lia.append(row[10])
		tot_assets.append(row[11])
		curr_assets.append(row[12])
		net_cash_flow.append(row[13])
		pb.append(row[14])
		price.append(row[15])

print name[0]

name_1=[]
symbol_1=[]
ti_1=[]
sales_1=[]
iffs_1=[]
eoi_1=[]
te_1=[]
cogs_1=[]
pat_1=[]
borow_1=[]
curr_lia_1=[]
tot_assets_1=[]
curr_assets_1=[]
net_cash_flow_1=[]
pb_1=[]
price_1=[]
#reading the second file
with open(sys.argv[2]) as f:
	lines = f.readlines()

neglect=0
for line in lines:
	neglect+=1
	row=line.split(',')
	if(neglect>4):
		name_1.append(row[0])
		symbol_1.append(row[1])
		ti_1.append(row[2])
		sales_1.append(row[3])
		iffs_1.append(row[4])
		eoi_1.append(row[5])
		te_1.append(row[6])
		cogs_1.append(row[7])
		pat_1.append(row[8])
		borow_1.append(row[9])
		curr_lia_1.append(row[10])
		tot_assets_1.append(row[11])
		curr_assets_1.append(row[12])
		net_cash_flow_1.append(row[13])
		pb_1.append(row[14])
		price_1.append(row[15])

# print int(sales[3])-int(sales[2])
print float(sales[3])

# for 



