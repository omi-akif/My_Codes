#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})


# In[3]:


df


# In[6]:


df.dropna()


# In[7]:


df.dropna(axis=1)


# In[60]:


df.dropna(thresh=2)


# In[9]:


df


# In[14]:


df.fillna(value=df.mean())


# In[16]:


df['A']


# In[17]:


df['A'].fillna(value=df["A"].mean())


# In[18]:


import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[19]:


data


# In[20]:


df1=pd.DataFrame(data)


# In[21]:


df1


# In[22]:


df1.groupby("Company")


# In[23]:


grp=df1.groupby("Company")


# In[24]:


grp


# In[25]:


grp.sum()


# In[26]:


df1


# In[27]:


grp.count()


# In[28]:


grp.describe()


# In[33]:


grp.describe().transpose()["FB"]


# In[34]:


grp.sum()


# In[35]:


grp.mean()


# In[36]:


grp.max()


# In[37]:


grp.min()


# In[38]:


grp.median()


# In[39]:


grp.mad()


# In[40]:


grp.var()


# In[41]:


grp.std()


# In[42]:


grp.skew()


# In[44]:


grp.cumsum()


# In[45]:





# In[46]:


df


# In[47]:


df.hist()


# In[50]:


import matplotlib as plt


# In[51]:


df.hist()


# In[61]:


import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# In[64]:


df["col2"].unique()


# In[ ]:




