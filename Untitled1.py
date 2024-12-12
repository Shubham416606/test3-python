#!/usr/bin/env python
# coding: utf-8

# In[3]:


#####reverse######
e1=open('ex1.txt')
data=e1.read()
data=data[::-1]
r1=open('reverse.txt','w+')
r1.write(data)
r1.seek(0)
print(r1.read())
r1.close()
e1.close()


# In[5]:


# to convret all char of text file in upper case
e1=open('ex1.txt')
data=e1.read()
data=data.upper()
print(data)


# In[7]:


e1=open('ex1.txt')
print(e1.readline())
print(e1.readline())
print(e1.read())


# In[9]:


e1=open('ex1.txt')
line=e1.readline()
for l in line:
    print(l)
e2=open('ex1.txt')
for i in e2:
    print(i)
    
    
    
# s
# h
# u
# b
# h
# a
# m
# shubham


# In[16]:


###['shubham']####
with open('ex1.txt')as e3:
    data=e3.read()
    data=data.split()
    print(data)
    


# In[29]:


#####reverse######
with open('ex1.txt')as e3:
    data=e3.read()
    data=data.split()
    s=''
    for word in data:
        word=word[::-1]
        s=s+' '+word
        ##or##
    print(s,end='')


# In[ ]:




