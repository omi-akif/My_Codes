#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[]


# In[2]:


type(a)


# In[3]:


b=()


# In[4]:


type(b)


# In[5]:


c={}


# In[6]:


type(c)


# In[7]:


city=["Dhaka","Chattagram","Barishal","Khulna","Rangpur","Rajshahi"]


# In[8]:


city


# In[9]:


city[0]


# In[10]:


city[:]


# In[12]:


city[:1]


# In[13]:


city[2:]


# In[15]:


city[2:4]


# In[19]:


lst1=[1,2,3,5,6,"b",[1,2,3,4,5]]


# In[21]:


lst1[6]


# In[25]:


lst1[6][:2]


# In[26]:


lst2=[1,2,3,4,5,6]


# In[28]:


lst3=["a","b","c"]


# In[33]:


lst4=lst2+lst3


# In[34]:


print(lst4)


# In[41]:


lst5=lst2*2


# In[39]:


lst5


# In[42]:


city.append("Cumilla")


# In[43]:


print(city)


# In[45]:


city.count("Dhaka")


# In[46]:


city.extend("Dhaka")


# In[47]:


city


# In[48]:


city.index("Khulna")


# In[52]:


city.insert(0,"Feni")


# In[53]:


city


# In[58]:


city.pop(0)


# In[59]:


city


# In[60]:


city.remove("D")


# In[61]:


city


# In[62]:


city.reverse()


# In[63]:


city


# In[64]:


city.sort()


# In[65]:


city


# In[66]:


city2=["Dhaka","Barishal","Khulna"]


# In[67]:


city2.sort()


# In[68]:


city2


# In[70]:


city2*5


# In[71]:


name=input("Enter Your Name:   ")


# In[72]:


print(name)


# In[73]:


city3="Chattagram"


# In[77]:


city3[4:6]


# In[80]:


city4=("Dhaka","Khalna") #tuple


# ## city4

# In[84]:


city2[0]="Chattagram"


# In[85]:


city2


# In[86]:


city4[2]="Feni"


# In[87]:


city5=[1,1,1,1,1,1,2,3,3,4,5,6,7,8,9,6]


# In[89]:


city5


# In[90]:


city6={1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 6}


# In[91]:


city6


# In[ ]:




