#!/usr/bin/env python
# coding: utf-8

# In[13]:


ex1=open('ex1.txt','w+')
print(ex1.write('welcome'))
ex1.close()
#print(ex1.read())


# In[5]:


ex2=open('ex2.txt','r+')
print(ex2.write('abc'))
ex2=open('ex2.txt','r')
print(ex2.read())
#ex2.close()


# In[13]:


ex1=open('ex1.txt','a')
ex1.write('abc')
# ex2=open('ex1.txt','r')
# print(ex1.read())
ex2.close()

#out-->welcomeabcabc


# In[15]:


ex1=open('ex1.txt','a+')
print(ex1.read())


# In[23]:


#####seek######## 
ex1=open('ex1.txt','a+')
ex1.seek(0)
ex1.seek(2)
print(ex1.read())


# In[ ]:


#user input
with open('ex3.txt','w+')as ex3:
    #ex3.write('ewlcome to the python')
    ex3.write(input())
    ex3.close
    


# In[3]:


with open('ex1.txt')as ex1:
    data=ex1.read()
    with open('ex2.txt','a')as ex2:
        ex2.write('\n')
        ex2.write(data)
        ex2.close
    f=open(ex2.txt)
    print(f.read())
    


# In[ ]:




