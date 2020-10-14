#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from numpy.random import randn
np.random.seed(101)


# In[3]:


from pandas import DataFrame


# In[4]:


df=DataFrame(randn(4,5),["A","B","C","D"],["V","W","X","Y","Z"])


# In[5]:


df


# In[7]:


df[['X','Y']]


# In[11]:


df.iloc[0]


# In[15]:


df["New"]=df["W"]+df["Y"]


# In[ ]:





# In[14]:


df


# In[22]:


df.drop("New",axis=1,inplace=True)


# In[23]:


df


# In[24]:


df.drop("D",axis=0)


# In[25]:


df


# In[26]:


df.loc[["A","B"]]


# In[27]:


df.loc["B"]["Y"]


# In[29]:


df.loc[["A","B"]][["X","Y"]]


# In[30]:


type(df)


# In[32]:


df.shape


# In[36]:


dr=df[df>0]       


# In[37]:


dr.dropna()


# In[39]:


dr


# In[43]:


df[df['W']>0]


# In[41]:





# In[48]:


df>0


# In[49]:


df[df>0]


# In[50]:


df["V"]>0


# In[52]:


df[df["V"]>0]


# In[55]:


df[df['W']>0]['V']


# In[54]:


df


# In[56]:


df=pd.read_csv("USA_Housing.csv")


# In[58]:


df.info()


# In[59]:


df.head()


# In[70]:


df.describe().transpose()


# In[72]:


dr1=df["Avg. Area Income"]


# In[73]:


dr1.sum()


# In[76]:


dr1.median()


# In[78]:


dr1.kurtosis()


# In[79]:


dr1.skew()


# In[80]:


dr1.std()


# In[81]:


dr1.var()


# In[ ]:




