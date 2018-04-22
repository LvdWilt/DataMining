###############################################################################################
# Swetta Jansen, Jerome Mies & Lotte van der Wilt
# Data Mining Project
#
# addSleep.py
#
# Takes times from raw data, ignores automatic data saves and finds the maximum time interval
# between phone use. This interval in hours is used as a measure for sleep time and added to
# the pre-processed data set.
###############################################################################################

import pandas as pd
import datetime
import numpy as np

data = pd.read_csv('C:\\Users\\Lotte\\Desktop\\Data mining\\dataset_mood_smartphone.csv')

participant=0

p = []
dt=[]
day =[]

# save dataframe with only datetime, day and participant
for ID in pd.unique(data["id"]):
    participant = participant+1
    first = True
    for date in pd.unique(data["time"][data["id"]==ID]):
        p.append(participant)
        dt.append(date)
        # count days where first day is 0
        if first:
            day.append(0)
            firstDay = date
            first = False
        else:
            day.append((datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S.%f").date() - datetime.datetime.strptime(firstDay, "%Y-%m-%d %H:%M:%S.%f").date()).days)

matrix = np.matrix([p,dt,day]).T
headers = ["Participant","Time","Day"]

df = pd.DataFrame(data = matrix,columns = headers)

df.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_times.csv")
data = pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_times.csv")

# add column for time
data["Times"] = pd.to_datetime(data["Time"])
data["Times"] = [time.time() for time in data["Times"]]

sleep=[]
p=[]
days=[]

for ID in pd.unique(data["Participant"]):
    firstday = min(data["Day"][data["Participant"]==ID])
    lastday = max(data["Day"][data["Participant"]==ID])

    # find the longest interval between phone use -> use as indication of sleep
    for day in range(lastday+1):
        last=pd.to_datetime("01-01-01 00:00:00").time()
        y = datetime.timedelta(hours=last.hour, minutes=last.minute, seconds=last.second, microseconds=last.microsecond)
        last=y
        longest=y-y
        if day in data["Day"][data["Participant"]==ID].values:
            First=True
            for time in sorted(data["Times"][data["Day"]==day][data["Participant"]==ID]):
                x = datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second, microseconds=time.microsecond)
                # don't count automatic logs (happen each hour at the hour exactly)
                if time.minute==0 and time.second==0:
                    temp=y-y
                else:
                    temp = (x-y)
                    y=x
                    if First:
                        morning=temp
                        first=False
                if temp>longest:
                    longest=temp
            # add first and last interval together (in case of sleep before midnight)
            night=morning+(last-y)
            if night>longest:
                longest=night
            sleep.append(longest)
            days.append(day)
            p.append(ID)

# save to new file
matrix = np.matrix([p,days,sleep]).T
headers = ["Participant","Day","Sleep"]
df = pd.DataFrame(data = matrix,columns = headers)
df.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\sleep.csv")
data=pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_onlyTargets.csv",index_col=0)

# add sleep to existing dataset
data["Sleep"]=np.nan

for ID in pd.unique(data["Participant"]):
    for day in pd.unique(data["Day"][data["Participant"]==ID]):
        time=pd.to_datetime(df["Sleep"][df["Participant"]==ID][df["Day"]==int(day)].values[0])
        minutes=time.hour+time.minute/60
        print(minutes)
        data["Sleep"][(data["Participant"]==ID) & (data["Day"]==day)]=minutes
print(data)
data.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_withSleep.csv")
