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

print name[10],name_1[10],eoi[10],eoi_1[10]
print len(name),len(name_1)
# converting spaces and NA to zero  AND typecasting to int
for i in range(0,len(name)):
	if sales[i] == '' or sales[i] == 'NA':
		sales[i] = 0
	sales[i]=float(sales[i])

	if ti[i] == '' or ti[i] == 'NA':
		ti[i] = 0
	ti[i]=float(ti[i])

	if iffs[i] == '' or iffs[i] == 'NA':
		iffs[i] = 0
	iffs[i]=float(iffs[i])

	if eoi[i] == '' or eoi[i] == 'NA':
		eoi[i] = 0
	eoi[i]=float(eoi[i])

	if te[i] == '' or te[i] == 'NA':
		te[i] = 0
	te[i]=float(te[i])

	if cogs[i] == '' or cogs[i] == 'NA':
		cogs[i] = 0
	cogs[i]=float(cogs[i])

	if pat[i] == '' or pat[i] == 'NA':
		pat[i] = 0
	pat[i]=float(pat[i])

	if borow[i] == '' or borow[i] == 'NA':
		borow[i] = 0
	borow[i]=float(borow[i])

	if curr_lia[i] == '' or curr_lia[i] == 'NA':
		curr_lia[i] = 0
	curr_lia[i]=float(curr_lia[i])

	if tot_assets[i] == '' or tot_assets[i] == 'NA':
		tot_assets[i] = 0
	tot_assets[i]=float(tot_assets[i])

	if curr_assets[i] == '' or curr_assets[i] == 'NA':
		curr_assets[i] = 0
	curr_assets[i]=float(curr_assets[i])

	if net_cash_flow[i] == '' or net_cash_flow[i] == 'NA':
		net_cash_flow[i] = 0
	net_cash_flow[i]=float(net_cash_flow[i])

	if pb[i] == '' or pb[i] == 'NA':
		pb[i] = 0
	pb[i]=float(pb[i])

	if price[i] == '' or price[i] == 'NA' or price[i]=='\n'or price[i]=='NA\n':
		price[i] = 0
	price[i]=float(price[i])

# for the second file
for i in range(0,len(name_1)):
	if sales_1[i] == '' or sales_1[i] == 'NA':
		sales_1[i] = 0
	sales_1[i]=float(sales_1[i])

	if ti_1[i] == '' or ti_1[i] == 'NA':
		ti_1[i] = 0
	ti_1[i]=float(ti_1[i])

	if iffs_1[i] == '' or iffs_1[i] == 'NA':
		iffs_1[i] = 0
	iffs_1[i]=float(iffs_1[i])

	if eoi_1[i] == '' or eoi_1[i] == 'NA':
		eoi_1[i] = 0
	eoi_1[i]=float(eoi_1[i])

	if te_1[i] == '' or te_1[i] == 'NA':
		te_1[i] = 0
	te_1[i]=float(te_1[i])

	if cogs_1[i] == '' or cogs_1[i] == 'NA':
		cogs_1[i] = 0
	cogs_1[i]=float(cogs_1[i])

	if pat_1[i] == '' or pat_1[i] == 'NA':
		pat_1[i] = 0
	pat_1[i]=float(pat_1[i])

	if borow_1[i] == '' or borow_1[i] == 'NA':
		borow_1[i] = 0
	borow_1[i]=float(borow_1[i])

	if curr_lia_1[i] == '' or curr_lia_1[i] == 'NA':
		curr_lia_1[i] = 0
	curr_lia_1[i]=float(curr_lia_1[i])

	if tot_assets_1[i] == '' or tot_assets_1[i] == 'NA':
		tot_assets_1[i] = 0
	tot_assets_1[i]=float(tot_assets_1[i])

	if curr_assets_1[i] == '' or curr_assets_1[i] == 'NA':
		curr_assets_1[i] = 0
	curr_assets_1[i]=float(curr_assets_1[i])

	if net_cash_flow_1[i] == '' or net_cash_flow_1[i] == 'NA':
		net_cash_flow_1[i] = 0
	net_cash_flow_1[i]=float(net_cash_flow_1[i])

	if pb_1[i] == '' or pb_1[i] == 'NA':
		pb_1[i] = 0
	pb_1[i]=float(pb_1[i])

	if price_1[i] == '' or price_1[i] == 'NA' or price_1[i]=='\n' or price_1[i]=='NA\n':
		price_1[i] = 0
	price_1[i]=float(price_1[i])


score=[]
for i in range(0,len(name_1)):
	if symbol_1[i] in symbol:
		index=symbol.index(symbol_1[i])
		score.append(0)
		score[i]+=1 if ( (ti_1[i]-eoi_1[i])/tot_assets_1[i] ) >0 else 0 #ROA
		score[i]+=1 if ( (ti_1[i]-eoi_1[i])/tot_assets_1[i] ) > ( (ti[index]-eoi[index])/tot_assets[index] )  else 0 #D_ROA
		score[i]+=1 if ( net_cash_flow_1[i]/tot_assets_1[i] ) >0 else 0 #CFO
		score[i]+=1 if ( net_cash_flow_1[i]/tot_assets_1[i] > (ti_1[i]-eoi_1[i])/tot_assets_1[i] )  else 0 #ACCRUAL
		score[i]+=1 if ( curr_assets_1[i]/curr_lia_1[i] ) >  ( curr_assets[index]/curr_lia[index] ) else 0 #D_LIQUID
		score[i]+=1 if ( borow_1[i]/tot_assets_1[i] ) < ( borow[index]/tot_assets[index] ) else 0 #D_LEVER
		if sales_1[i] == 0 :#D_MARGIN AND D_TURNOVER
			score[i]+=1 if ( (iffs_1[i]-te_1[i])/iffs_1[i] ) >( (iffs[index]-te[index])/iffs[index] ) else 0 
			score[i]+=1 if ( iffs_1[i]/tot_assets_1[i] ) >( iffs[index]/tot_assets[index] ) else 0
		else:
			score[i]+=1 if ( (sales_1[i]-cogs_1[i])/sales_1[i] ) >( (sales[index]-cogs[index])/sales[index] ) else 0
			score[i]+=1 if ( sales_1[i]/tot_assets_1[i] ) >( sales[index]/tot_assets[index] ) else 0

	else:
		score.append(-10)
	print score[i], name_1[i]
		# assign score to neg