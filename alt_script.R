#Piotroski in R
datafile <- read.csv(commandArgs(trailingOnly = FALSE)[6],sep =',',stringsAsFactors=FALSE)
useful_info <- datafile[c(3,4),-c(1)]
datafile <- datafile[-(0:4),]
names <- t(datafile[,1])
datafile <- datafile[,-c(1)]
datafile <- as.data.frame(sapply(datafile,as.numeric))
datafile[is.na(datafile)] <- 0
rownames(datafile) <- names
useful_info[1,] <- substr(useful_info[1,],nchar(useful_info[1,])-1,nchar(useful_info[1,]))
prefix_list <- factor(unlist(c(useful_info[1,])))
levels(prefix_list) <- c('n','h','p','c','f')
adnames <- paste(prefix_list,unlist(c(useful_info[2,])),sep="")
colnames(datafile) <- adnames
score<-	rep(0,nrow(datafile)+1)
score<- score +  c(0,((datafile['cTotal income']-datafile['cTotal expenses']-datafile['cExtra-ordinary income']+datafile['cExtra-ordinary expenses'])/datafile['pTotal assets'] >0 ))
score<- score +  c(0,( (datafile['cTotal income']-datafile['cTotal expenses']-datafile['cExtra-ordinary income']+datafile['cExtra-ordinary expenses'])/datafile['pTotal assets'] ) > ( (datafile['pTotal income']-datafile['pTotal expenses']-datafile['pExtra-ordinary income']+datafile['pExtra-ordinary expenses'])/datafile['hTotal assets'] ) )
score<- score +  c(0,( datafile['cNet cash flow from operating activities']/datafile['pTotal assets']  >0) )
score<- score +  c(0,(( (datafile['cTotal income']-datafile['cTotal expenses']-datafile['cExtra-ordinary income']+datafile['cExtra-ordinary expenses'])/datafile['pTotal assets'] ) < ( datafile['cNet cash flow from operating activities']/datafile['pTotal assets'] )) )
score<- score +  c(0,(datafile['cCurrent ratio (times)'] >   datafile['pCurrent ratio (times)']) )
score<- score +  c(0,(( datafile['cTotal term liabilities']/datafile['cAverage total assets'] ) < ( datafile['pTotal term liabilities']/datafile['pAverage total assets'] )) )
for(i in 1:nrow(datafile)){
	if(datafile[i,'pNet sales']*datafile[i,'cNet sales'] == 0){
	score[c(1,i+1)]<- score[c(1,i+1)] +  c(0,(( (datafile[i,'cNet sales']-datafile[i,'cCost of goods sold'])/datafile[i,'cNet sales'] ) >( (datafile[i,'pNet sales']-datafile[i,'pCost of goods sold'])/datafile[i,'pNet sales'] )) )
	score[c(1,i+1)]<- score[c(1,i+1)] +  c(0,(( datafile[i,'cAverage total assets']/datafile[i,'cNet sales'] ) <( datafile[i,'pAverage total assets']/datafile[i,'pNet sales'] )) )
	}
	else{
	score[c(1,i+1)]<- score[c(1,i+1)] +  c(0,(( (datafile[i,'cIncome from financial services']-datafile[i,'cCost of goods sold'])/datafile[i,'cIncome from financial services'] ) >( (datafile[i,'pIncome from financial services']-datafile[i,'pCost of goods sold'])/datafile[i,'pIncome from financial services'] )) )
	score[c(1,i+1)]<- score[c(1,i+1)] +  c(0,(( datafile[i,'cAverage total assets']/datafile[i,'cIncome from financial services'] ) <( datafile[i,'pAverage total assets']/datafile[i,'pIncome from financial services'] )) )
}
}
datafile['Fscore'] = score[-c(1)]
for(i in 1:ncol(datafile)){datafile[,i]<-replace(datafile[,i],is.infinite(datafile[,i]),NA)}
for(i in c('cAdjusted Opening Price ','fAdjusted Closing Price ')){datafile[,i]<-replace(datafile[,i],datafile[,i]==0,NA)}
datafile <- datafile[complete.cases(datafile),]
highbm <- datafile[order(datafile[,'cP/B ']),][1:(nrow(datafile)/2),]
bottom_decile <-highbm[order(highbm[,'Fscore']),][1:(nrow(highbm)/10),]
top_decile <-highbm[order(highbm[,'Fscore']),][1:(9*nrow(highbm)/10),]
top_returns <- sum((top_decile[,'fAdjusted Closing Price ']-top_decile[,'cAdjusted Opening Price '])/top_decile[,'cAdjusted Opening Price '])/nrow(top_decile)
bottom_returns <- sum((-bottom_decile[,'fAdjusted Closing Price ']+bottom_decile[,'cAdjusted Opening Price '])/bottom_decile[,'cAdjusted Opening Price '])/nrow(bottom_decile)
returns <- top_returns+bottom_returns
print(returns)