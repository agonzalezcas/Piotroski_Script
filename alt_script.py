import csv
import sys

# Transpose of a list
def transpose(alist):
	return map(list, zip(*alist))

# Read and store in 2D Array
datafile = open(sys.argv[1],'r')
# datafile = open("2006d.csv",'r') for example
datareader = csv.reader(datafile, delimiter =",")
data = list(datareader)
del data[0:5]
for i in xrange(0,len(data)):
	for j in xrange(2,len(data[i])):
		try:
			data[i][j] = float(data[i][j])
		except:
			data[i][j] = 0.0

dictionary = {row[1]:row[0:1]+row[2:] for row in data}
# Calculate F_SCORE
f_score = []
companies_for_removal =[]
# 0 name, 1 symbol, 2 ti, 3 sales, 4 finan-income, 5 eoincome, 6 totexpen, 7 cogs, 8 borrow, 9 curlia, 10 totas, 11 curass, 12 cflw
#                 14 ti, 15 sales, 16 finan-income, 17 eoincome, 18 totexpen, 19 cogs, 20 borrow, 21 curlia, 22 totas, 23 curass, 24 cflw
# 25 p/b ,26 mcap, 27 mcapfut
for company in data:
	try:
		score =0
		score+=1 if ( (company[14]-company[17])/company[22] ) >0 else 0 #ROA
		score+=1 if ( (company[14]-company[17])/company[22] ) > ( (company[2]-company[5])/company[10] )  else 0 #D_ROA
		score+=1 if ( company[24]/company[22] ) >0 else 0 #CFO
		score+=1 if ( company[24]/company[22] > ( company[14]-company[17])/company[22])  else 0 #ACCRUAL
		score+=1 if ( company[23]/company[21] ) >  ( company[11]/company[9] ) else 0 #D_LIQUID
		score+=1 if ( company[20]/company[22] ) < ( company[8]/company[10] ) else 0 #D_LEVER
		try:#D_MARGIN
			score+=1 if ( (company[15]-company[19])/company[15] ) >( (company[3]-company[7])/company[3] ) else 0
		except:
			score+=1 if ( (company[16]-company[18])/company[16] ) >( (company[4]-company[6])/company[4] ) else 0 

		try:#D_TURNOVER
			score+=1 if ( company[15]/company[22] ) >( company[3]/company[10] ) else 0
		except:
			score+=1 if ( company[16]/company[22] ) >( company[4]/company[10] ) else 0
		f_score.append(score)
	except:
		companies_for_removal.append(company)

for company in companies_for_removal:
	data.remove(company)

data = transpose(data)
data.append(f_score)
data = transpose(data)

# Sorted by BM
bmsorted_data = sorted(data, key = lambda x: x[25])
# Take top 50%
highbm_data =[i for j,i in enumerate(bmsorted_data) if j in range(0, len(bmsorted_data)/2)]
# Sorted by f_score
fsorted_data = sorted(highbm_data, key = lambda x: x[28])
bottom_decile =[i for j,i in enumerate(fsorted_data) if j in range(0, 1 + len(fsorted_data)/10)]
# bottom_decile = transpose(bottom_decile)
top_decile =[i for j,i in enumerate(fsorted_data) if j in range(9*len(fsorted_data)/10, len(fsorted_data))]
# top_decile = transpose(top_decile)
returns = 0
for company in top_decile:
	returns+= (company[27]-company[26])/company[26]
for company in bottom_decile:
	returns+= (company[26]-company[27])/company[26]
returns =  (returns*15/100) + 7
print returns