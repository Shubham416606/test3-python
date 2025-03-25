#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
cities =['ahmdavad','surat','rajkot','mumbai']
ds = pd.Series(cities)
print(ds)
print(type(ds))


# In[8]:


x=[10,20,30]
ds1=pd.Series(x)
print(ds1)


# In[12]:


marks = [10,20,30,40]
ds1 = pd.Series(marks,index=['A','B','C','D'],name="RESULT")
print(ds1)
ds1.size
type(ds1)
ds1.name


# In[30]:


import pandas as ps
data={'calries':[420,400,350,450],'duration':[50,45,40,44]}
dt = pd.DataFrame(data)
print(dt)
dt.to_csv('file2.csv')
type(dt)


# In[24]:


dt.loc[0]


# In[25]:


dt[0::]


# In[26]:


dt[::]


# In[27]:


dt[::1]


# In[29]:


dt.loc[[0,1]]


# In[32]:


import pandas as ps
data={'calries':[420,400,350,450,350,500,580,700,750],'duration':[50,45,40,44,45,85,15,26,36]}
dt = pd.DataFrame(data)
print(dt)
dt.to_csv('file2.csv')
type(dt)


# In[35]:


dataset = pd.read_csv('file2.csv')
print(dataset)


# In[37]:


dataset.shape


# In[39]:


dataset.head()


# In[40]:


dataset.tail()


# In[41]:


dataset.head(2)


# In[43]:


dataset.tail(2)


# In[44]:


dataset.info()


# In[45]:


dataset.describe()


# In[48]:


dataset = pd.read_csv("file2.csv",index_col="calries",squeeze=True)
print(dataset)
type(dataset)


# In[50]:


dataset = pd.read_csv("file2.csv")
print(dataset)
type(dataset)


# In[ ]:


dataset = pd.read_csv('diabetes.csv')
print(dataset)
type(dataset)


# In[51]:


dataset.head(6)


# In[52]:


dataset.tail(6)


# In[53]:


dataset.info()


# In[1]:


dataset.describe()


# In[13]:


import numpy as np
import pandas as pd
data= {"name":["Williams","Emma","Sofia","Markus","Edward","Thomas","Ethan",np.nan,"Arun","Anika","Paulo"],
       "region":[np.nan,"North","East",np.nan,"West","South",np.nan,"West","East","South"],
       "Sales":[50000,52000,np.nan,np.nan,42000,72000,49000,np.nan,67000,65000,67000],
        "Expences":[42000,43000,np.nan,np.nan,38000,29000,42000,np.nan,39000,50000,45000]}

df=pd.DataFrame(data)
df


# In[14]:


df.isna().sum()#Checking null data


# In[15]:


df.dropna(thresh=2)


# In[17]:


df.dropna() #Remove all rows with any number of null


# In[18]:


df.dropna(how="all") #if all value is null


# In[22]:


df.dropna(subset=["Sales","Expences"]) #drop any sales & expenses are null


# In[23]:


df.dropna(axis=0)


# In[24]:


df.dropna(axis=1)


# In[26]:


df["Sales"]


# In[27]:


df["Sales"].fillna(0)


# In[31]:


df[Sales].fillna(df["Sales"].mean())


# In[30]:


dataset=pd.read_csv("auto-mpf.csv")
print(dataset)
type(dataset)


# In[ ]:


import pandas as pd
df=pd read_csv("auto-mpg.csv")
df


# In[ ]:


df shape #398,9


# In[38]:


df[df["horsepower"]=="?"]


# In[ ]:


Finding and Removing outliers 


# In[ ]:


Q1=df["npy"].quantile(0.25)
Q3=df["npy"].quantile(0.75)
Iqr=Q3-Q1=58-52=6
Low=Q1-1.5*Iqr=
High=Q3+1.5*Iqr=


# In[4]:


import pandas as pd
df=pd.read_csv("sales_data.csv")
print(df)


# In[5]:


df['sales'].fillna(0.0)


# In[6]:


df['sales'].fillna(df['sales'].mean().median())


# In[9]:


import pandas as pd
df=pd.read_csv("auto-mpg.csv")
df


# In[19]:


import pandas as pd
df=pd.read_csv("auto-mpg.csv")

q1=df['acceleration'].quantile(0.25)
q3=df['acceleration'].quantile(0.75)
iqr=q3-q1
low_val=q1-1.5*iqr
high_val=q3+1.5*iqr
print(high_val,low_val)
df2=df.loc[(df['acceleration']<low_val)|(df['acceleration']>high_val)]
print(df2)
df3=df.loc[(df['acceleration']>=low_val)&(df['acceleration']<=high_val)]
print(df3)


# In[27]:


import pandas as pd
data={'A':['A','B','B','C','A'],
           'B':[50,40,40,30,50],
      'C':['True','False','False','False','True']
     }

df=pd.DataFrame(data)
print(df)
dups=df.duplicated()
print(dups)
df_d=df.drop_duplicates()
print(df_d)
df_d=df_d.reset_index(drop=True)
print(df_d)


# In[35]:


import pandas as pd
ipl=pd.read_csv("ipl-matches.csv")
print(df)
ipl[ipl['SuperOver']=='Y'].shape[0]



# In[32]:


ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]


# In[33]:


ipl[(ipl['City']=='Kolkata')&(ipl['WinningTeam']=='Chennai Super Kings')].shape[0]


# In[34]:


ipl[(ipl['Player_of_Match']=='HH Pandya')&((ipl['Team1']=='Rajasthan Royals')|(ipl['Team2']=='Rajasthan Royals'))].shape[0]


# In[2]:


import pandas as pd
df=pd.read_csv("diabetes_unclean - Copy - Copy.csv")
print(df)


# In[3]:


df.describe(include=object)


# In[4]:


df.shape[0]


# In[6]:


df.isna().sum()


# In[11]:


df['HbA1c']=df['HbA1c'].fillna(df['HbA1c'].mean())
df=df.dropna()
df.isna().sum()


# In[12]:


df.info()


# In[13]:


df.corr()


# In[15]:


import matplotlib.pyplot as plt
c=['AGE', 'Urea', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']
plt.boxplot(df[c])
plt.show()


# In[18]:


pd.plotting.parallel_coordinates(df,'AGE',['Urea','HbA1c','TG','BMI'])
plt.show()


# In[23]:


df=df[df['Gender']!='f']
print(df.shape)
pd.crosstab(df['Gender'],df['CLASS'])


# In[447]:


import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
g.add_node(1)
g.add_nodes_from([2,3])
#g.add_nodes_from(range(4,7))
g.add_edge(1,2)
g.add_edges_from([(1,2),(2,3),(3,4),(4,1)])
nx.draw_networkx(g,node_size=850,node_color='red',width=5,edge_color='blue')
plt.show()


# In[1]:


import matplotlib.pyplot as plt
x=range(1,6)
y=[1,4,6,8,4]
plt.fill_between(x,y,color='skyblue',alpha=0.2)
plt.plot(x,y,color='red')
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
months=np.arange(12)
income=np.array([5,9,6,6,10,7,6,4,4,5,6,4])
expense=np.array([6,6,8,3,6,9,7,8,6,6,4,8])
fig,ax=plt.subplots(figsize=(8,8))
ax.plot(months,income,color='green')
ax.plot(months,expense,color='red')
ax.fill_between(months,income,expense,where=(income>expense),color='green',label='positive',alpha=0.3,interpolate=True)
ax.fill_between(months,income,expense,where=(income<expense),color='red',label='negative',alpha=0.3,interpolate=True)
plt.xlabel('months')
plt.ylabel('income/expense comparison')
plt.legend()
plt.show()


# In[11]:


import matplotlib.pyplot as plt
import numpy as np
x=range(1,6)
y1=[1,4,6,8,9]
y2=[2,2,7,10,12]
y3=[2,8,5,10,6]
plt.stackplot(x,y1,y2,y3,labels=['A','B','C'],colors=['red','blue','green'])
plt.legend(loc='upper left')
plt.show()


# In[16]:


import matplotlib.pyplot as plt
import numpy as np
from pywaffle import Waffle
import pandas as pd
data={'phone':['apple','samsung','1+','realme','oppo'],
     'stock':[44,12,8,5,50]}
df=pd.DataFrame(data)
fig=plt.figure(FigureClass=Waffle,rows=10,values=df.stock,labels=list(df.phone))


# In[18]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
stopwords=set(STOPWORDS)
f=open('alice.txt',encoding='utf8')
a=f.read()
a_wc=WordCloud(background_color='white',max_words=2000)
stopwords.add('said')
a_wc.generate(a)
plt.imshow(a_wc)
plt.axis('off')
plt.show()


# In[ ]:




