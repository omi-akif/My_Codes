#%%
import pandas as pd 
import seaborn as sns 
import numpy as np
from pandas import DataFrame, read_csv
#%%
h=pd.read_csv('F:/Codes/Python/CSV_Files/tips.csv')
#%%
h.tail(10)
#%%
s = pd.Series(np.nan, index= np.arange(10))
#%%
s
#%%
h.head(10)
#%%
air = pd.read_csv('F:/Codes/Python/CSV_Files/air.csv')
#%%
air.head(10)
#%%
crash = pd.read_csv('F:/Codes/Python/CSV_Files/crash.csv')
#%%
crash.head(10)
#%%
crash.loc[500:510]
#%%
air.loc[0]
#%%
air['Value']
#%%
c = sns.distplot(air['Value'])
#%%
c = sns.distplot(air['Value'], kde = True, bins = 1, rug = False, norm_hist = True)
#%%
star = pd.read_csv(filepath_or_buffer = 'F:/Codes/Python/CSV_Files/star0000-1.csv', index_col = False)
#%%
df = DataFrame(crash, np.arange(11))
#%%
df1 = DataFrame(star, columns = np.arange(11), index = np. arange(2173761))
#%%
df1
#%%
df.loc[0]
#%%
df.set_index([[0]])
#%%
sns.distplot(star['266'])
#%%
sns.distplot(star[0:2], kde = True)
#%%
sns.jointplot(x='speeding', y='alcohol', data = crash2, kind = 'kde')
#%%
crash2 = sns.load_dataset('car_crashes')
#%%
crash2 
#%%
sns.distplot(crash2['total'], kde = True, bins = 10)
#%%
sns.jointplot(x='speeding',y='alcohol',data=crash2, kind='reg')
#%%
sns.pairplot(crash2)
#%%
sns.barplot(x='speeding', y = 'alcohol', data = crash2, kde = True)
#%%
crash2.index
#%%
df2 = DataFrame(air)
#%%
sns.boxplot(x='speeding',y='alcohol', data = crash2, hue = 'ins_premium')
#%%
sns.violinplot(x='speeding', y = 'alcohol', data = crash2, hue = 'ins_premium')
#%%
sns.swarmplot(x='speeding', y = 'alcohol', data = crash2)
#%%
