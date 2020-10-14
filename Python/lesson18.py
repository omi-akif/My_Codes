#%%
double = lambda double:double/2
#%%
my_list = [1,2,3,4,5,6,7,8,9]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
#%%
new_list
#%%
#Hirearchial Indexing
import numpy as np
import pandas as pd
from pandas import DataFrame
data  = pd.Series(np.random.randn(10), index = [['a','a','a', 'b', 'b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,1,2]])
#Unsolved

#%%
#Hadof
#PySpark
#map()
data