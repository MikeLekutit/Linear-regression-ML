#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[25]:


data = pd.read_csv(r'C:\Users\mikes\Downloads\insurance.csv')


# In[26]:


data.head()


# In[27]:


data.describe()


# In[28]:


data.tail()


# In[30]:


data.shape


# In[31]:


data.columns


# In[32]:


data.nunique()


# In[34]:


data['sex'].unique()


# In[35]:


data['bmi'].unique()


# In[36]:


data.isnull().sum()


# In[38]:


client = data.drop(['children'], axis=1)


# In[39]:


client.head()


# In[47]:


#relationship analysis


# In[48]:


import seaborn as sns


# In[49]:


corelation = client.corr()


# In[50]:


sns.heatmap(corelation, xticklabels = corelation.columns,yticklabels = corelation.columns, annot = True)


# In[51]:


sns.pairplot(client)


# In[52]:


sns.relplot(x= 'age', y='charges', hue='smoker',data=client)


# In[53]:


sns.displot(client['bmi'])


# In[54]:


sns.catplot(x='region', y='charges', data=client)


# In[55]:


sns.catplot(x='charges', kind='box', data= client)


# In[ ]:




