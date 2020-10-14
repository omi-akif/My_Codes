#%%
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
%matplotlib inline
#%%
rcParams['figure.figsize']=15, 6
#%%
dt = pd.read_csv('G:/Codes/Python/air.csv')
print(dt)
dt.head
dt.dtypes
#%%
dt.index
#%%
datPa = lambda d: pd.datetime.strptime(d, '%Y-%m')
dt = pd.read_csv('G:/Codes/Python/air.csv', parse_dates=['Month'], index_col='Month', date_parser=datPa)
#%%
dt.index
#%%
dft = pd.DataFrame(data=dt)
#%%
dft.index
#%%
dft.loc['1949-01-01']
#%%
dft.loc['1949-01-01':'1949-05-01']
#%%
dft.loc['1949']
#%%
plt.plot(dft)
#Overall increasing trend along with some seasonal variations
#%%
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
#%%
staTest(dft)
#%%
ts_log = np.log(dft)
plt.plot(ts_log)
#%%
import pandas
moving_avg=ts_log.rolling(12, win_type='triang').mean()
plt.plot(ts_log)
plt.plot(moving_avg, color='white')
#%%
ts_log_moving_avg_diff = ts_log-moving_avg
ts_log_moving_avg_diff.head(12)

#%%
ts_log_moving_avg_diff.dropna(inplace=True)
staTest(ts_log_moving_avg_diff)

#%%
#expwighted_avg = ts_log.ewm(halflife = 12.00)
#plt.plot(ts_log)
#plt.plot(expwighted_avg, color='red')