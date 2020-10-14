#%%
import pandas as pd
import seaborn as sns
tips=pd.read_csv('F:/Codes/Python/CSV_Files/titanic.csv')

tips.head()
#%%
sns.distplot(tips['fare'])
#%%
sns.distplot(tips['fare'],kde=True,bins=200)
sns.jointplot(x='fare',y='survived',data=tips,kind='kde')
tips
#%%
sns.jointplot(x='fare',y='survived',data=tips,kind='reg')
sns.pairplot(tips)
#%%
sns.barplot(x='survived',y='fare',data=tips)
sns.countplot(x='survived', data=tips)
#%%
sns.boxplot(x='age',y='fare', data=tips)
sns.violinplot(x='age',y='fare')

#%%
sns.boxplot(x='fare',y='age', data=tips,hue='survived')
#%%
sns.violinplot(x='age',y='fare', data=tips, hue='survived')
#%%
sns.violinplot(x='age',y='fare', data=tips)
#%%
sns.stripplot(x='age',y='fare', data=tips, hue='survived')
#%%
sns.swarmplot(x='age',y='fare',data=tips)
#%%
sns.violinplot(x='age',y='fare',data=tips)
sns.swarmplot(x='age',y='fare',data=tips, color='black')
#%%
sns.lmplot(x='fare',y='survived',data=tips)
#%%
sns.lmplot(x='fare',y='survived',data=tips, col='survived')
#%%
sns.lmplot(x='fare',y='survived',data=tips, hue='time')
#%%
sns.lmplot(x='survived',y='fare', data=tips, hue='survived')
#%%
sns.distplot(tips['survived'],kde=True, bins=50)
#%%
sns.distplot(tips['survived'],kde=True,bins=100)
#%%
sns.jointplot(x='fare',y='survived',data=tips,kind='kde')
tips
#%%
sns.jointplot(x='survived',y='fare',data=tips,kind='kde')
#%%
tips.iloc[0]