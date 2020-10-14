#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')


# In[97]:


rcParams['figure.figsize']=15, 6


# In[98]:


dt = pd.read_csv('air.csv')
print(dt)
dt.head
dt.dtypes


# In[99]:


dt.index


# In[100]:


datPa = lambda d: pd.datetime.strptime(d, '%Y-%m')
dt = pd.read_csv('air.csv', parse_dates=['Month'], index_col='Month', date_parser=datPa)


# In[101]:


dt.index


# In[102]:


dft = pd.DataFrame(data=dt)


# In[103]:


dft.index


# In[104]:


dft.index


# In[105]:


dft.loc['1949-01-01']


# In[106]:


dft.loc['1949-01-01':'1949-05-01']


# In[107]:


plt.plot(dft)
#Overall increasing trend along with some seasonal variations


# In[108]:


from statsmodels.tsa.stattools import adfuller
def staTest(ts):
    plt.legend(loc='best')
    plt.title('The Rolling Mean and the standard deviation')

    rllMn = dft.rolling(12).mean()
    #pd.rolling_mean(ts, window=12)
    rllStd = dft.rolling(12).std()
    #pd.rolling_std(ts, window = 12)
    Osh = plt.plot(ts, label='Showing Original...', color = 'blue')
    mn = plt.plot(rllMn, color = 'red', label = 'The Rolling Mean')
    std = plt.plot(rllStd, color='white', label='The Rolling Standard Deviation')
    plt.show(block=False)

    #print('Dicky Fuller Test -- Results')
    #tstDF = adfuller(ts, autolag='AIC') 
    #outDF = pd.Series(tstDF[0:4], index=['dft', - 'p-valuee', '#Lags Use d', 'Number of Observatoin Used'])
    #for key,value in tstDF[4].items():
    #outDF['Critical Value (%s)' %key] = value
    #print (outDF) #


# In[109]:


staTest(dft)


# In[110]:


ts_log = np.log(dft)
plt.plot(ts_log)


# In[111]:


import pandas
moving_avg=ts_log.rolling(12, win_type='triang').mean()
plt.plot(ts_log)
plt.plot(moving_avg, color='white')


# In[112]:


ts_log_moving_avg_diff = ts_log-moving_avg
ts_log_moving_avg_diff.head(12)


# In[113]:


ts_log_moving_avg_diff.dropna(inplace=True)
staTest(ts_log_moving_avg_diff)


# In[115]:




