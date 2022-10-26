#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn import preprocessing 


# # Start Divar Project 

# In[15]:


#import csv file


# In[2]:


divar = pd.read_csv('divar_ads_dataset-2 22.51.36.csv')


# In[6]:


divar


# In[16]:


#remove extra column 


# In[3]:


divar.drop('Unnamed: 0', axis=1,inplace=True)


# In[10]:


divar


# In[17]:


#finding min data


# In[12]:


divar.describe()


# In[13]:


minid = divar['id'].min()
divar['id'][divar['id']==minid]


# In[14]:


#missing values 


# In[18]:


divar.isnull()


# In[19]:


divar.isnull().sum()


# In[3]:


divar.fillna({'year':1400,'brand':'Unknown',}, inplace=True)
divar


# In[4]:


divar['mileage'].fillna(value=divar.mileage.mean())


# In[14]:


#find & drop duplicate Data


# In[12]:


divar.duplicated()


# Let's drop a column 

# In[20]:


divar.drop_duplicates(['city'])


# In[21]:


divar.describe()


# In[ ]:


#finding count of different values 


# In[23]:


divar.cat2.value_counts()


# In[6]:


divar.mileage.value_counts()


# In[6]:


divar.city.value_counts()


# Find the value of the desired variable

# In[5]:


#groupby desire value for analysis data by different categories 


# In[29]:


group=divar.groupby(divar['cat2'])
group
group.mean()


# In[9]:


#Let's make a crosstab


# In[30]:


pd.crosstab(divar.cat2,divar.city)


# In[10]:


#Let's make 2 different pivot_Tables


# In[34]:


pd.pivot_table(divar,index='cat2',columns='city',values='id')


# In[36]:


pd.pivot_table(divar,index='cat2',columns='id',values='image_count')


# In[6]:


divar.insert(0,'Rank',list(range(1,947636)))


# In[7]:


divar['price'].replace({-1:3800040},inplace=True)


# In[5]:


divar


# In[11]:


#chart section 


# In[17]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sb


# In[8]:


df=pd.DataFrame(divar.price)


# In[18]:


plt.figure(figsize=(40,15),dpi=120)
df=pd.DataFrame(divar.price)
df.boxplot()


# In[16]:


plt.figure(figsize=(60,15),dpi=150)
sb.stripplot(x='cat2',y='price',data=divar,size=15)
plt.show()


# In[7]:


plt.figure(figsize=(40,15),dpi=120)
plt.plot(divar['Rank']/10000,divar['price']/100000,color='mediumpurple')

plt.show()


# In[ ]:


#plt.pie(divar.Rank, labels=divar.city)
#plt.show()


# # End of Project 

# In[ ]:




