import pandas as pd
import numpy as np 
from numpy.random import randn 
np.random.seed(101)
from pandas import DataFrame
df=DataFrame(randn(4,5),['A','B','C','D'],['V','W','X','Y','Z'])
print(df)
print(df[['V','Y']])
print(df.iloc[2])
print(df.iloc[[1]])
print(df.iloc[[2]])
print(df.iloc[[3]])
df['New']=df['W']+df['Y']
print(df)
df.drop('New',axis=1,inplace=True)
print(df)
df.drop('Z',axis=1,inplace=True)
print(df)
c=df.loc[['A','B']]
print(c)
sf=DataFrame(np.arange(12).reshape(3,4),columns=['A','B','C','D'])
sf.drop(['B','C'], axis=1,inplace=True)
print(sf)
print(df.loc[['A','B']])
print(df)
v=df.loc[['A','B']]
print(v)
print(df)
s=df.iloc[[1,3]]
print(s)
n=df.loc[['A','B'],['V','W']]
print(n)
t=df.loc["B"]["Y"]
print(t)
print(type(df))
print(df.shape)
print(df>0)
print(df[df>0])
print(df.shape)
dr=df[df>0]
dr.dropna()
print(dr.dropna())

print(df[df['V']>0])
print(df>0)

print(df)
#print(df[['V','W']])
#print(df[df['W']>0])
print(df[df['W']>0]['V'])
print(df.iloc[:3][2:])
import csv
cs=pd.read_csv('data.csv')
print(cs.info())
print(cs.head())
#print(cs.describe().transpose())
dr1=cs["Balance"]
print(dr1.sum())
print(dr1.median())
print(dr1.kurtosis())
print(dr1.skew())
print(dr1.std())
print(dr1.var())