#!/usr/bin/env python
# coding: utf-8

# Python Logical Oparetors 
# 

# In[1]:


x=5
y=6


# In[2]:


x==5 and y==6


# In[4]:


x==6 and y==5


# In[5]:


x==5 and y==7


# In[6]:


x==5 or y==7


# In[7]:


x==7 or y==6


# In[8]:


x==7 or y==9


# In[11]:


not (x==5 and y==6)


# # Conditionals
# 

# In[13]:


x=4


# In[14]:


if x % 2 == 0:
    print(x,"is a even number.")


# In[17]:


x=5


# In[19]:


if x % 2 == 0:
    print(x,"is a even number.")
else:
    print(x,"is a odd number.")


# In[ ]:





# In[3]:


y=2001


# In[4]:


if y % 4 == 0:
    print(y,"is a leap year")
else:
    print(y, "is not a leap year")


# In[11]:


x=72


# In[12]:


if x >= 97:
    print("A+")
elif x>= 90:
    print("A")
elif x>=87:
    print("B+")
elif x>=83:
    print("B")
elif x>=80:
    print("B-")
elif x>=77:
    print("C+")
elif x>=73:
    print("C")
elif x>=70:
    print("C")
else:
    print("F")


# For Loop
# 

# In[14]:


saarc=["Bangladesh","India","Pakisthan","Sri Lanka","Nepal","Bhutan","Maldives","Afganisthan"]


# In[15]:


saarc


# In[20]:


for x in saarc:
    print(x, "is a very active member of Saarc")


# In[22]:


for x in range(101):
    print(x)


# In[26]:


for x in range(0,101,5):
    print(x)


# In[ ]:




