#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Regression Plots
# 
# Seaborn has many built-in capabilities for regression plots, however we won't really discuss regression until the machine learning section of the course, so we will only cover the **lmplot()** function for now.
# 
# **lmplot** allows you to display linear models, but it also conveniently allows you to split up those plots based off of features, as well as coloring the hue based off of features.
# 
# Let's explore how this works:

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tips = sns.load_dataset('tips')


# In[3]:


tips.head()


# ## lmplot()

# In[5]:


sns.lmplot(x='total_bill',y='tip',data=tips)


# In[6]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')


# In[13]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')


# ### Working with Markers
# 
# lmplot kwargs get passed through to **regplot** which is a more general form of lmplot(). regplot has a scatter_kws parameter that gets passed to plt.scatter. So you want to set the s parameter in that dictionary, which corresponds (a bit confusingly) to the squared markersize. In other words you end up passing a dictionary with the base matplotlib arguments, in this case, s for size of a scatter plot. In general, you probably won't remember this off the top of your head, but instead reference the documentation.

# In[16]:


# http://matplotlib.org/api/markers_api.html
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})


# ## Using a Grid
# 
# We can add more variable separation through columns and rows with the use of a grid. Just indicate this with the col or row arguments:

# In[28]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[30]:


sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)


# In[24]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm')


# ## Aspect and Size
# 
# Seaborn figures can have their size and aspect ratio adjusted with the **size** and **aspect** parameters:

# In[36]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)


# You're probably wondering how to change the font size or control the aesthetics even more, check out the Style and Color Lecture and Notebook for more info on that!
# 
# # Great Job!