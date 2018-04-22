###############################################################################################
# Swetta Jansen, Jerome Mies & Lotte van der Wilt
# Data Mining Project
#
# deleteNaN.py
#
# Manually remove NaN variables per participant, if attribute used.
###############################################################################################

import pandas as pd
import numpy as np

data=pd.read_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_withSleep.csv",index_col=0)

# each participant as seperate dataframe
p1 = data[data["Participant"]==1];p2 = data[data["Participant"]==2];p3 = data[data["Participant"]==3];p4 = data[data["Participant"]==4]
p5 = data[data["Participant"]==5];p6 = data[data["Participant"]==6];p7 = data[data["Participant"]==7];p8 = data[data["Participant"]==8]
p9 = data[data["Participant"]==9];p10 = data[data["Participant"]==10];p11 = data[data["Participant"]==11];p12 = data[data["Participant"]==12]
p13 = data[data["Participant"]==13];p14 = data[data["Participant"]==14];p15 = data[data["Participant"]==15];p16 = data[data["Participant"]==16]
p17 = data[data["Participant"]==17];p18 = data[data["Participant"]==18];p19 = data[data["Participant"]==19];p20 = data[data["Participant"]==20]
p21 = data[data["Participant"]==21];p22 = data[data["Participant"]==22];p23 = data[data["Participant"]==23];p24 = data[data["Participant"]==24]
p25 = data[data["Participant"]==25];p26 = data[data["Participant"]==26];p27 = data[data["Participant"]==27]

attribute = "Activity"                      # used attribute
p1 = p1[np.isnan(p1[attribute])==False]     # example

# concatenate all dataframes
frames = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27]
total = pd.concat(frames)
total.to_csv("C:\\Users\\Lotte\\Desktop\\Data mining\\list_nonNA.csv")
