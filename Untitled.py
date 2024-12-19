#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
os.getcwd()
os.chdir('D:\\temp\\shubham')
os.getcwd()
f=open('New Text Document.txt','w+')
f.write('my name is shubham')
f.close()


# In[8]:


get_ipython().run_cell_magic('writefile', 'cal.py', 'def sam(a,b):\n    return a+b\ndef sub(a,b):\n    return a-b')


# In[20]:


from cal import sam
sam(1,2)
from os import getcwd
import os
os.getcwd()


# In[24]:


print(dir())
os.getcwd()
print(os.listdir())


# In[25]:


import os as osss

