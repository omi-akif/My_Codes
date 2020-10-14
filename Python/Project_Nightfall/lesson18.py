#%%
import numpy as np
import pandas as pd
#%%
dset = pd.read_csv('TimeUse.csv')
#%%
dset
#%%
df= pd.read_csv('TimeUse.csv', index_col=0)
