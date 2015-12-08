import csv 
with open('out.csv') as f:
	lines = f.readlines()


# read everything
for line in lines:
	row=line.split(',')
	print row[0]
# do the calculations



#ftotal is the total score
