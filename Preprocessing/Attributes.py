###############################################################################################
# Swetta Jansen, Jerome Mies & Lotte van der Wilt
# Data Mining Project
#
# Attributes.py
#
# make a table for how often each attribute is used in best attribute vectors per participant
# up to length 5
###############################################################################################

import pandas as pd

# create empty table
data = pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\Attribute selection\\Participant18.csv",index_col=0,nrows=5)
for col in ["Mood", "Valence", "Sleep", "Activity", "Arousal", "Participant", "Screen", "Calls", "SMS", "Entertainment","Finance", "Communication","Games","Office","Social","Travel","Weather","Utilities","Mood..t.1.","Mood..t.2.","Mood..t.3.","Mood..t.4.","Valence..t.1.", "Valence..t.2.","Valence..t.3.","Arousal..t.1.","Arousal..t.2.","Arousal..t.3.","Activity..t.1.","Activity..t.2.","Activity..t.3.","Screen..t.1.","Screen..t.2.","Screen..t.3."]:
    data[col]=0
del data["(Intercept)"]

# add one to table at appropriate place for each time the attribute is used
for i in range(27):
    filename = ("C:\\Users\\Lotte\\Desktop\\Data mining\\Attribute selection\\Participant"+str(i+1)+".csv")
    temp=pd.read_csv(filename,index_col=0)
    for col in ["Mood", "Valence", "Sleep", "Activity", "Arousal", "Participant", "Screen", "Calls", "SMS", "Entertainment","Finance", "Communication","Games","Office","Social","Travel","Weather","Utilities","Mood..t.1.","Mood..t.2.","Mood..t.3.","Mood..t.4.","Valence..t.1.", "Valence..t.2.","Valence..t.3.","Arousal..t.1.","Arousal..t.2.","Arousal..t.3.","Activity..t.1.","Activity..t.2.","Activity..t.3.","Screen..t.1.","Screen..t.2.","Screen..t.3."]:
        for index in range(5):
            if temp[col][index+1]==True:
                data[col][index+1] = data[col][index+1]+ 1

# save to new file
data.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\Attribute selection\\Attributes.csv")
