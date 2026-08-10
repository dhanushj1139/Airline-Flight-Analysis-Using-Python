# -*- coding: utf-8 -*-


#Import library


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""**Data reading**"""

df=pd.read_csv("/content/airlines_flights_data.csv")

df.tail()
df.shape
df.columns
df.head()

df.info()

df.describe()

df.columns

df.isna().sum()

df.duplicated().sum()

"""**outliers check**

"""

q1=df['price'].quantile(0.25)
q3=df['price'].quantile(0.75)
iqr=q3-q1
ll=q1-(1.5*iqr)
ul=q3+(1.5*iqr)
min=df['price'].min()
max=df['price'].max()
print(min>ll)
print(max)
print(ul)

plt.boxplot(df['price'])
plt.show()

"""*after analysing i found some outliers here so by using clapping method we can replace the outliers

"""

df['price'].clip(lower=ll,upper=ul,inplace=True)

plt.boxplot(df['price'])
plt.show()

"""outliers in durations"""

plt.boxplot(df['duration'])
plt.show()

"""*after analysing i found in duration also we have outliers"""

q1=df['duration'].quantile(0.25)
q3=df['duration'].quantile(0.75)
iqr=q3-q1
ll=q1-(1.5*iqr)
ul=q3+(1.5*iqr)
min=df['duration'].min()
max=df['duration'].max()
print(min>ll)
print(max)
print(ul)

"""*here by using clapping method i can replace the outliers"""

df['duration'].clip(lower=ll,upper=ul,inplace=True)

"""*after replacing the outliers"""

plt.boxplot(df['duration'])
plt.show()

df[df['price']=='']

row=df.select_dtypes(include=object).columns
df[row]=df[row].apply(lambda x:x.str.strip().str.lower().str.title())

df.head()

df.groupby(by=df['departure_time'])['airline'].count()

sns.countplot(data=df,x=df['departure_time'],hue=df['airline'],palette={"Spicejet":"#eb4d31","Airasia":"#f79f8f","Vistara":"#7a1173","Go_First":"#2727f5","Indigo":"#5bcdf0","Air_India":"#872d09"})
plt.title("count of flights vs day")
plt.ylabel("flight count")
plt.xlabel("day sessions")
plt.show()

sns.lineplot(data=df,x=df['departure_time'],y=df['price'],hue=df['airline'],palette={"Spicejet":"#eb4d31","Airasia":"#f79f8f","Vistara":"#7a1173","Go_First":"#2727f5","Indigo":"#5bcdf0","Air_India":"#872d09"})
plt.legend(loc="upper right",ncol=2)
plt.title("ticket_amount vs Day Sessions")
plt.xlabel("Day Sessions")
plt.show()

df.groupby(df['airline'])['price'].sum()

sns.barplot(data=df,x=df['airline'],y=df['price'],estimator,palette={"Spicejet":"#eb4d31","Airasia":"#f79f8f","Vistara":"#7a1173","Go_First":"#2727f5","Indigo":"#5bcdf0","Air_India":"#872d09"})
plt.title("Total_amount VS Airline")
plt.ylabel("total_amount    units(crore)")
plt.show()

total_amount=df.groupby(df['departure_time'])['price'].sum()

plt.pie(total_amount,autopct="%1.1f%%",labels=total_amount.index)
plt.title("total amount Vs Day Sessions")
plt.show()





