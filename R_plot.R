library(data.table)
library(ggplot2)
library(plyr)
library(scales)

setwd("/Users/Al/Documents/cs597/Selfish-Mining-Study/R_CSVs/")
data<- fread("results100.csv")
data$startEnd<- with(data,paste(startHeight,endHeight))
# small<- data[sample(seq(1,nrow(data)),1000),]

# ggplot(data,aes(startHeight,count,group=startHeight))+geom_boxplot()+theme(legend.position="none")
tmp<- ddply(data,.(startHeight,type,seqLength,pool),summarize,count.mean=mean(count),count.sd=sd(count))
obs<- subset(tmp,type=="Observed")
sim<- subset(tmp,type!="Observed")
mrged<- merge(obs,sim,by = c('startHeight','seqLength','pool'),suffixes = c('.obs','.sim'))
mrged$diff<- with(mrged,count.mean.obs-count.mean.sim)
mrged$num.sds<- with(mrged,diff/count.sd.sim)
#View(subset(mrged,num.sds>1))

ggplot(mrged,aes(abs(diff),group=seqLength,color=as.factor(seqLength)))+stat_ecdf()+scale_x_continuous(breaks=pretty_breaks(10))
