############################################################################################################################
# Swetta Jansen, Jerome Mies & Lotte van der Wilt
# Data Mining Project
#
# attributes_individual.R
#
# Finds best attributes for each participant seperately through multiple regression. Saves attribute tables as well as R^2 
# and BIC.
############################################################################################################################

# read in data and select non NaN
data = read.csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_withSleep.csv",header = T)
data<-na.omit(data)

library(MASS)
library(leaps)
library(car)

# matrix for R^2 and BIC values
rsq=matrix(0L,nrow=27,ncol=33)
bic=matrix(0L,nrow=27,ncol=33)

for (i in 1:27){
  p = subset(data,Participant==i)
  # multiple regression, find best attribute vector for each vector size
  leaps<-regsubsets(Target~Mood+Valence+Sleep+Activity+Arousal+Participant+Screen+Calls+SMS+Entertainment+Finance+Communication+Games+Office+Social+Travel+Weather+Utilities+Mood..t.1.+Mood..t.2.+Mood..t.3.+Mood..t.4.+Valence..t.1.+Valence..t.2.+Valence..t.3.+Arousal..t.1.+Arousal..t.2.+Arousal..t.3.+Activity..t.1.+Activity..t.2.+Activity..t.3.+Screen..t.1.+Screen..t.2.+Screen..t.3.,nvmax=35,data=p,nbest=1)
  temp=summary(leaps)$"rsq"
  temp2=summary(leaps)$"bic"
  # if smaller than max length fill rest with NA values (to prevent errors when writing to file)
  while (length(temp)<33){
    temp=append(temp,NA)
    temp2=append(temp2,NA)}
  rsq[i,]=temp
  bic[i,]=temp2
  attr=summary(leaps)$"which"
  # save attribute table to file
  write.csv(attr,paste("participant",i,".csv",sep=""))
}

# save R^2 and BIC values to file
write.csv(rsq,paste("rsq.csv",sep=""))
write.csv(bic,paste("bic.csv",sep=""))
