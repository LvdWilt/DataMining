###############################################################################################
# Swetta Jansen, Jerome Mies & Lotte van der Wilt
# Data Mining Project
#
# preprocessing.py
#
# Preprocessing of phone dataset. Converting to daily values, calculation of mean and SD for
# each variable and each participant, remove data with NaN mood or target.
###############################################################################################

import pandas as pd
import numpy as np
import datetime

#-------------------------------------Part 1: Keep date and remove times from timestamp--------------------------------------#
data = pd.read_csv('C:\\Users\\Lotte\\Desktop\\Data mining\\dataset_mood_smartphone.csv', index_col=0)

# remove time from datetime
for i,row in data.iterrows():
    data["time"][i] = row["time"][:10]

data.to_csv('C:\\Users\\Lotte\\Desktop\\Data mining\\dataset_mood_smartphone_dates.csv')
#------------------------------------Part 2: Data set with daily values for all variables------------------------------------#
data = pd.read_csv('C:\\Users\\Lotte\\Desktop\\Data mining\\dataset_mood_smartphone_dates.csv',index_col=0)

participant=0

# create empty arrays for daily values for each participant
p = []; day = []; mood = []; valence = []; arousal = []; activity = []; screen = []; calls = []; SMS = []; entertainment = []
finance = []; communication = []; games = []; office = []; social = []; travel = []; utilities = []; weather = []

for ID in pd.unique(data["id"]):
    participant = participant+1
    first = True

    for date in pd.unique(data["time"][data["id"]==ID]):
        p.append(participant)
        # count days (where the first day is 0)
        if first:
            day.append(0)
            firstDay = date
            first = False
        else:
            day.append((datetime.datetime.strptime(date,"%Y-%m-%d").date() - datetime.datetime.strptime(firstDay, "%Y-%m-%d").date()).days)

        # for mood, take daily mean
        if date in data["time"][data["variable"]=="mood"][data["id"]==ID].values:
            mood.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="mood"].mean())
        else:
            mood.append(np.nan)

        # for valence, take daily mean
        if date in data["time"][data["variable"]=="circumplex.valence"][data["id"]==ID].values:
            valence.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="circumplex.valence"].mean())
        else:
            valence.append(np.nan)

        # for arousal, take daily mean
        if date in data["time"][data["variable"]=="circumplex.arousal"][data["id"]==ID].values:
            arousal.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="circumplex.arousal"].mean())
        else:
            arousal.append(np.nan)

        # for activity, take daily mean
        if date in data["time"][data["variable"]=="activity"][data["id"]==ID].values:
            activity.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="activity"].mean())
        else:
            activity.append(np.nan)

        # for screen time, take daily sum
        if date in data["time"][data["variable"]=="screen"][data["id"]==ID].values:
            screen.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="screen"].sum())
        else:
            screen.append(0)

        # for calls, take daily sum
        if date in data["time"][data["variable"]=="call"][data["id"]==ID].values:
            calls.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="call"].sum())
        else:
            calls.append(0)

        # for SMS messages, take daily sum
        if date in data["time"][data["variable"]=="sms"][data["id"]==ID].values:
            SMS.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="sms"].sum())
        else:
            SMS.append(0)

        # for duration of communication app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.communication"][data["id"]==ID].values:
            communication.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.communication"].sum())
        else:
            communication.append(0)

        # for duration of entertainment app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.entertainment"][data["id"]==ID].values:
            entertainment.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.entertainment"].sum())
        else:
            entertainment.append(0)

        # for duration of financial app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.finance"][data["id"]==ID].values:
            finance.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.finance"].sum())
        else:
            finance.append(0)

        # for duration of game app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.game"][data["id"]==ID].values:
            games.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.game"].sum())
        else:
            games.append(0)

        # for duration of office app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.office"][data["id"]==ID].values:
            office.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.office"].sum())
        else:
            office.append(0)

        # for duration of social app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.social"][data["id"]==ID].values:
            social.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.social"].sum())
        else:
            social.append(0)

        # for duration of travel app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.travel"][data["id"]==ID].values:
            travel.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.travel"].sum())
        else:
            travel.append(0)

        # for duration of utilities app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.utilities"][data["id"]==ID].values:
            utilities.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.utilities"].sum())
        else:
            utilities.append(0)

        # for duration of weather app usage, take daily sum
        if date in data["time"][data["variable"]=="appCat.weather"][data["id"]==ID].values:
            weather.append(data["value"][data["time"]==date][data["id"]== ID][data["variable"]=="appCat.weather"].sum())
        else:
            weather.append(0)

# save data to new CSV file
matrix = np.matrix([p,day,mood,valence,arousal,activity,screen,calls,SMS,entertainment,finance,communication,games,office,social,travel,utilities,weather]).T
headers = ["Participant","Day","Mood","Valence","Arousal","Activity","Screen","Calls","SMS","Entertainment","Finance","Communication","Games","Office","Social","Travel","Utilities","Weather"]
df = pd.DataFrame(data = matrix,columns = headers)
df.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list.csv")


#--------------------------------------------Part 3: Remove data where mood is NaN-------------------------------------------#

fulldata = pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list.csv")

# remove data where mood is NaN
data=fulldata[pd.notna(fulldata["Mood"])]

data.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_nonzero.csv")

#------------------------------------------Part 4: Save mean and SD for each variable----------------------------------------#

means = np.zeros((27,16))
SDs = np.zeros((27,16))
count_a=0
score=np.zeros((1268,16))
headers=[]
days=np.zeros(1268)
part=np.zeros(1268)

# For each attribute, for each participant find the mean and standard deviation.
for attribute in ["Mood","Valence","Arousal","Activity","Screen","Calls","SMS","Communication","Entertainment","Finance","Games","Office","Social","Travel","Utilities","Weather"]:
    headers.append(attribute)
    count_p=0
    count=0

    for ID in pd.unique(data["Participant"]):
        mean = data[attribute][data["Participant"]==ID].mean()
        sd = np.std(data[attribute][data["Participant"]==ID])
        means[count_p,count_a] = mean
        SDs[count_p,count_a] = sd
        # scale all variables according to participant mean and standard deviations
        for day in data["Day"][data["Participant"]==ID]:
            score[count,count_a]=(data[attribute][data["Participant"]==ID][data["Day"]==day]-mean)/sd
            if count_a == 0:
                days[count]=day
                part[count]=ID
            count = count+1
        count_p = count_p+1
    count_a = count_a+1

m = pd.DataFrame(data=means,columns=headers)
s = pd.DataFrame(data=SDs,columns=headers)

new1=np.matrix([part,days]).T
new2=np.matrix(score)

# scaled list (mean 0, sd 1) -> not used after choosing model for each participant
scaled=pd.DataFrame(data=np.hstack([new1,new2]),columns=["Participant","Day","Mood","Valence","Arousal","Activity","Screen","Calls","SMS","Communication","Entertainment","Finance","Games","Office","Social","Travel","Utilities","Weather"])

# save dataframe of means and standard deviations as well as a list where all parameters are scaled
m.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\means.csv")
s.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\sds.csv")
scaled.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\scaled_list.csv")


#-------------------------------------------Part 5: Add targets and previous values------------------------------------------#

data = pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_nonzero.csv")

# arrays for all new attributes (previous and target)
Target=np.zeros(1268);MoodM1=np.zeros(1268);MoodM2=np.zeros(1268);MoodM3=np.zeros(1268);MoodM4=np.zeros(1268)
MoodM5=np.zeros(1268);MoodM6=np.zeros(1268);ValenceM1=np.zeros(1268);ValenceM2=np.zeros(1268);ValenceM3=np.zeros(1268)
ArousalM1=np.zeros(1268);ArousalM2=np.zeros(1268);ArousalM3=np.zeros(1268);ActivityM1=np.zeros(1268);ActivityM2=np.zeros(1268)
ActivityM3=np.zeros(1268);ScreenM1=np.zeros(1268);ScreenM2=np.zeros(1268);ScreenM3=np.zeros(1268)

count = 0

for ID in pd.unique(data["Participant"]):
    days = len(data[data["Participant"]==ID])
    last = int(max(data["Day"][data["Participant"]==ID].values))+1
    daynums=data["Day"][data["Participant"]==ID].values

    # if there are no missing days for participants, simple shift in variable array
    if last == days:
        Target[count:count+days] = np.hstack([data["Mood"][data["Participant"]==ID][data["Day"]>daynums[0]],np.zeros(1)])          # t+1
        MoodM1[count:count+days] = np.hstack([np.zeros(1),data["Mood"][data["Participant"]==ID][data["Day"]<daynums[-1]]])         # t-1
        MoodM2[count:count+days] = np.hstack([np.zeros(2),data["Mood"][data["Participant"]==ID][data["Day"]<daynums[-2]]])         # t-2
        MoodM3[count:count+days] = np.hstack([np.zeros(3),data["Mood"][data["Participant"]==ID][data["Day"]<daynums[-3]]])         # t-3
        MoodM4[count:count+days] = np.hstack([np.zeros(4),data["Mood"][data["Participant"]==ID][data["Day"]<daynums[-4]]])         # t-4
        MoodM5[count:count+days] = np.hstack([np.zeros(5),data["Mood"][data["Participant"]==ID][data["Day"]<daynums[-5]]])         # t-5
        MoodM6[count:count+days] = np.hstack([np.zeros(6),data["Mood"][data["Participant"]==ID][data["Day"]<daynums[-6]]])         # t-6
        ValenceM1[count:count+days] = np.hstack([np.zeros(1),data["Valence"][data["Participant"]==ID][data["Day"]<daynums[-1]]])   # t-1
        ValenceM2[count:count+days] = np.hstack([np.zeros(2),data["Valence"][data["Participant"]==ID][data["Day"]<daynums[-2]]])   # t-2
        ValenceM3[count:count+days] = np.hstack([np.zeros(3),data["Valence"][data["Participant"]==ID][data["Day"]<daynums[-3]]])   # t-3
        ArousalM1[count:count+days] = np.hstack([np.zeros(1),data["Arousal"][data["Participant"]==ID][data["Day"]<daynums[-1]]])   # t-1
        ArousalM2[count:count+days] = np.hstack([np.zeros(2),data["Arousal"][data["Participant"]==ID][data["Day"]<daynums[-2]]])   # t-2
        ArousalM3[count:count+days] = np.hstack([np.zeros(3),data["Arousal"][data["Participant"]==ID][data["Day"]<daynums[-3]]])   # t-3
        ActivityM1[count:count+days] = np.hstack([np.zeros(1),data["Activity"][data["Participant"]==ID][data["Day"]<daynums[-1]]]) # t-1
        ActivityM2[count:count+days] = np.hstack([np.zeros(2),data["Activity"][data["Participant"]==ID][data["Day"]<daynums[-2]]]) # t-2
        ActivityM3[count:count+days] = np.hstack([np.zeros(3),data["Activity"][data["Participant"]==ID][data["Day"]<daynums[-3]]]) # t-3
        ScreenM1[count:count+days] = np.hstack([np.zeros(1),data["Screen"][data["Participant"]==ID][data["Day"]<daynums[-1]]])     # t-1
        ScreenM2[count:count+days] = np.hstack([np.zeros(2),data["Screen"][data["Participant"]==ID][data["Day"]<daynums[-2]]])     # t-2
        ScreenM3[count:count+days] = np.hstack([np.zeros(3),data["Screen"][data["Participant"]==ID][data["Day"]<daynums[-3]]])     # t-3
    # otherwise, manually check if each day exists, if so, copy the variable
    else:
        for i in daynums:
            index_i=count+list(daynums).index(i)
            i = int(i)
            mood=data["Mood"][data["Day"]==i][data["Participant"]==ID]
            valence=data["Valence"][data["Day"]==i][data["Participant"]==ID]
            arousal=data["Arousal"][data["Day"]==i][data["Participant"]==ID]
            activity=data["Activity"][data["Day"]==i][data["Participant"]==ID]
            screen=data["Screen"][data["Day"]==i][data["Participant"]==ID]
            if i-1 in daynums:
                Target[index_i-1] = data["Mood"][data["Day"]==i][data["Participant"]==ID]
            if i+1 in daynums:
                MoodM1[index_i+1]=mood
                ValenceM1[index_i+1]=valence
                ArousalM1[index_i+1]=arousal
                ActivityM1[index_i+1]=activity
                ScreenM1[index_i+1]=screen
            if i+2 in daynums:
                index=list(daynums).index(i+2)
                MoodM2[count+index]=mood
                ValenceM2[count+index]=valence
                ArousalM2[count+index]=arousal
                ActivityM2[count+index]=activity
                ScreenM2[count+index]=screen
            if i+3 in daynums:
                index=list(daynums).index(i+3)
                MoodM3[count+index]=mood
                ValenceM3[count+index]=valence
                ArousalM3[count+index]=arousal
                ActivityM3[count+index]=activity
                ScreenM3[count+index]=screen
            if i+4 in daynums:
                index=list(daynums).index(i+4)
                MoodM4[count+index]=mood
            if i+5 in daynums:
                index=list(daynums).index(i+5)
                MoodM5[count+index]=mood
            if i+6 in daynums:
                index=list(daynums).index(i+6)
                MoodM6[count+index]=mood
    count = count+days

# save data to new file
data["Target"]=Target;data["Mood (t-1)"]=MoodM1;data["Mood (t-2)"]=MoodM2;data["Mood (t-3)"]=MoodM3;data["Mood (t-4)"]=MoodM4
data["Mood (t-5)"]=MoodM5;data["Mood (t-6)"]=MoodM6;data["Valence (t-1)"]=ValenceM1;data["Valence (t-2)"]=ValenceM2
data["Valence (t-3)"]=ValenceM3;data["Arousal (t-1)"]=ArousalM1;data["Arousal (t-2)"]=ArousalM2;data["Arousal (t-3)"]=ArousalM3
data["Activity (t-1)"]=ActivityM1;data["Activity (t-2)"]=ActivityM2;data["Activity (t-3)"]=ActivityM3;data["Screen (t-1)"]=ScreenM1
data["Screen (t-2)"]=ScreenM2;data["Screen (t-3)"]=ScreenM3
data.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_includingT.csv")


#-------------------------------------------Part 6: Remove data where target is NaN------------------------------------------#

data = pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_includingT.csv",index_col=0)

data = data[data["Target"]>0]

data.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_onlyTargets.csv")

#----------------------------------------Part 7: Remove day if no days before or after---------------------------------------#

days=[]

for ID in pd.unique(data["Participant"]):
    firstday=min(data["Day"][data["Participant"]==ID].values)
    lastday=max(data["Day"][data["Participant"]==ID].values)
    longest=0
    for day in pd.unique(data["Day"][data["Participant"]==ID]):
        day = int(day)
        # remove data if no data 2 days before and 2 days after
        if day-1 in data["Day"][data["Participant"]==ID].values or day-2 in data["Day"][data["Participant"]==ID].values or day+2 in data["Day"][data["Participant"]==ID].values or day+1 in data["Day"][data["Participant"]==ID].values:
            days.append(day)
        else:
            data = data[(data["Participant"]!=ID) | (data["Day"]!=day)]
    days=[]

data.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\List_reducedColumns.csv")

