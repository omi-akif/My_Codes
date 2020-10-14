#!/usr/bin/env python
# coding: utf-8

# In[1]:


std1={}


# In[3]:


type(std1)


# In[5]:


std1["Name"]="Abrar Morshed"


# In[6]:


std1


# In[7]:


std1["Id"]=4554656
std1["Age"]=23


# In[8]:


std1


# In[11]:


std1["Name"]


# In[12]:


std2={"Name":"Ahad Mahmud","Age":23,"ID":2350485,"MIS101":"A","CSE101":"A+","MIS305":"A"}


# In[13]:


std2


# In[38]:


saarc={"Name":["Bangladesh","Afganisthan","Pakisthan","Nepal","Bhutan","India","Sri Lanka","Maldiv"],"GDP":[255364,75981,9753,74559,7456,78516,78954,98765],"Ppl":[41455,7575265,6575,578552,997,78564,457865,97865]}


# In[39]:


saarc


# In[35]:


import pandas as pd


# In[40]:


saarc=pd.DataFrame(saarc)


# In[41]:


saarc


# In[43]:


std3=std2.copy()


# In[44]:


std3


# In[45]:


std2.fromkeys("ID")


# In[48]:


std2.items()


# In[49]:


std2.keys()


# In[50]:


std2.pop("Name")


# In[51]:


std2


# In[54]:


std2.popitem()


# In[59]:


std2.update({"MIS101":"A+"})


# In[60]:


std2


# In[61]:


45>565


# In[62]:


535>454


# In[63]:


34<23


# In[65]:


43<45


# In[66]:


3==2


# In[67]:


3==3


# In[68]:


23!=2


# In[71]:


x=3
if x>2:
    print("OK")


# In[ ]:




