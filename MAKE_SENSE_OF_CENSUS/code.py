# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#step1
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("The shape of data is:",data.shape)
#Code starts here
census = np.concatenate((new_record,data),axis=0)
print("The shape of census is:",census.shape)

#step2
age = census[:,0]
print("age array: ",age)
max_age = age.max(axis=0)
print("Maximum age: ",max_age)
min_age = age.min()
print("Minimum age: ",min_age)
age_mean = age.mean()
print("Mean of the age: ",age_mean)
age_std = np.std(age)
print("standard deviation: ",age_std)

#step3

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = list(np.where(np.array([len_0,len_1,len_2,len_3,len_4])==(np.array([len_0,len_1,len_2,len_3,len_4])).min()))[0]
print(minority_race)

#step4
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print((avg_working_hours))

#step5
high=census[census[:,1]>10]
avg_pay_high=high[:,7].mean()
print(avg_pay_high)
low=census[census[:,1]<=10]
avg_pay_low=low[:,7].mean()
print(avg_pay_low)



