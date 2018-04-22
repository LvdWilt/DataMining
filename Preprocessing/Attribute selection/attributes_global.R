############################################################################################################################
# Swetta Jansen, Jerome Mies & Lotte van der Wilt
# Data Mining Project
#
# attributes_global.R
#
# Finds best attributes for the global dataset through multiple regression. 
############################################################################################################################

data = read.csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_withSleep.csv",header = T)
data<-na.omit(data)

library(MASS)
library(leaps)
library(car)

# Stepwise regression
fit <- lm(Target~Mood+Valence+Sleep+Activity+Arousal+Participant+Screen+Calls+SMS+Entertainment+Finance+Communication+Games+Office+Social+Travel+Weather+Utilities+Mood..t.1.+Mood..t.2.+Mood..t.3.+Mood..t.4.+Mood..t.5.+Mood..t.6.+Valence..t.1.+Valence..t.2.+Valence..t.3.+Arousal..t.1.+Arousal..t.2.+Arousal..t.3.+Activity..t.1.+Activity..t.2.+Activity..t.3.+Screen..t.1.+Screen..t.2.+Screen..t.3.,data=P1)
step <- stepAIC(fit, direction="both")
step$anova # display results

# All subsets regression
leaps<-regsubsets(Target~Mood+Valence+Sleep+Activity+Arousal+Participant+Screen+Calls+SMS+Entertainment+Finance+Communication+Games+Office+Social+Travel+Weather+Utilities+Mood..t.1.+Mood..t.2.+Mood..t.3.+Mood..t.4.+Valence..t.1.+Valence..t.2.+Valence..t.3.+Arousal..t.1.+Arousal..t.2.+Arousal..t.3.+Activity..t.1.+Activity..t.2.+Activity..t.3.+Screen..t.1.+Screen..t.2.+Screen..t.3.,nvmax=35,data=P1,nbest=1)
summary(leaps)
plot(leaps,scale="r2")
subsets(leaps, statistic="rsq",max.size=35)
summary(leaps)$"bic"
summary(leaps)$"rsq"

# (For values in between, manually change 'fit')
extractAIC(fit,k=2)
