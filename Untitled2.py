#!/usr/bin/env python
# coding: utf-8

# In[5]:


f=open('friends.txt')
for i in range(len(f.readlines())):
    f.seek(0)
    for j in range(i+1):
        line=f.readline()
        line=line[::-1]
    print(line)
        


# In[18]:


f=open('friends.txt')
lines=f.readline()
for line in line:
    if line[0]=='#':
        continue
    else:
        print(line)


# In[3]:


f=open('file1.txt')
d={}
data=g=f.read().split()
for i in data:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in data:
    print(i,'_',d[i],end='')


# In[5]:


#wap surch to a word from a text file at list position type word is not found if word is not found
e=open('file1.txt','r')
data=e.read()
word=input('enter word')
i=data.find(word)
if i==-1:
    print(word,'word is not found')
else:
    print(word,'word is found a position')


# In[3]:





# In[ ]:





# In[ ]:




