#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


x=np.linspace(1,5,10)


# In[7]:


y=x**2


# In[18]:


plt.plot(x,y, "red",linewidth=1,markersize=10, marker="+")
plt.xlabel("XLabel")
plt.ylabel("Y Label")
plt.title("First Chart")
plt.show()


# In[10]:


x


# In[19]:


y


# In[21]:


plt.scatter(x,y)
plt.xlabel("XLabel")
plt.ylabel("Y Label")
plt.title("First Chart")
plt.show()


# In[ ]:




