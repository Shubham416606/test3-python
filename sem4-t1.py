#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
cities=['ahemdabad','surat','rajkot']
ds=pd.Series(cities)
print(ds)
print(type(ds))


# In[6]:


marks=[10,20,30]
ds1=pd.Series(marks,index=['A','B','C'],name="result")
print(ds1)
ds1.size
print(type(ds1))
ds1.name


# In[17]:


import pandas as pd1
data={"cdories":[420,400,350,450,420,400,350,450],"duration":[50,45,40,44,50,45,40,44]}
df=pd1.DataFrame(data)
print(df)
df.to_csv('file1.csv')
print(type(df))
df.loc[[0,1]]
df[::2]


# In[18]:


import pandas
dataset=pd.read_csv('file1.csv')
print(dataset)
print(type(dataset))


# In[20]:


dataset.shape


# In[21]:


dataset.tail()


# In[26]:



dataset.head()


# In[28]:


dataset.info


# In[38]:


dataset=pd.read_csv('bollywood.csv',index_col='movie',squeeze=True)
print(dataset)
type(dataset)


# In[32]:


dataset=pd1.read_csv('diabetes.csv')
print(dataset)
dataset.head(6)
dataset.tail(6)
dataset.info
dataset.describe()


# In[9]:


import pandas as pd1
data={'A':[10,20,30,40],
     'B':[100,200,300,40]}
df=pd1.DataFrame(data)
print(df)


# In[3]:


df1=pd1.read_csv('auto-mpg (1).csv')
print(df1)


# In[16]:


print(df1.to_string())


# In[17]:


print(df1.loc[2])


# In[18]:


print(df1.loc[[1,2]])


# In[20]:


print(df1.iloc[:,0])


# In[21]:


print(df1.head(2))


# In[22]:


print(df1.tail())


# In[23]:


print(df1.info())


# In[24]:


print(df1.describe())


# In[25]:


print(df1.describe(include='all'))


# In[31]:


df1.corr()


# In[30]:


import matplotlib.pyplot as plt
pd1.plotting.scatter_matrix(df1,figsize=[20,20],marker='V',alpha=0.5)
plt.show()


# In[6]:


df1['horsepower']=pd1.to_numeric(df1['horsepower'].replace('?',0.0))
print(df1.to_string())


# In[34]:


df1.info()


# In[35]:


df1.corr()


# In[7]:


import matplotlib.pyplot as plt
import pandas as pd1
pd1.plotting.scatter_matrix(df1,figsize=[20,20],marker='V',alpha=0.5)
plt.show()


# In[9]:


import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
pll=parallel_coordinates(df1,'cylinders',
                        cols=['acceleration','mpg','origin','cylinders'],
                        color=['red','green','yellow','blue','orange'])


# In[15]:


import pandas as pd1
pd1.crosstab(df1['cylinders'],df1['model year'],rownames=['cylinders'],colnames=['model year'])


# In[35]:


import pandas as pd
df2=pd.read_csv("sales_data.csv")
print(df2)


# In[23]:


df2.isna().sum()


# In[25]:


df2.dropna()


# In[26]:


df2.dropna(thresh=2)


# In[27]:


df2.dropna(how='all')


# In[37]:


df2.dropna(subset=['sales','expenses'])
df2.dropna(axis=0)


# In[36]:


df2.dropna(axis=1)
print(df2)


# In[33]:


df2.dropna(inplace=True)
print(df2)


# In[ ]:





# In[ ]:




