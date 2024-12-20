#!/usr/bin/env python
# coding: utf-8

# In[1]:


class student:
    def f1(self):
        print('this is student')
        self.num1=int(input('enter num1 '))
        self.num2=int(input('enter num2 '))
    def f2(self):
        print('num1 ',self.num1)
        print('num2 ',self.num2)
       


# In[ ]:





# In[22]:


m=student()
m.f1()
m.f2()


# In[4]:


class factory:
    data=[]
    def a(s):
        s.name=input('enter name ')
        factory.data.append(s.name)
        s.price=int(input('enter price '))
        factory.data.append(s.price)
    def dis(s):
        print('name ',s.name)
        print('price ',s.price)
        print( factory.data)
        


# In[6]:


x=factory()
x.a()
x.dis()


# In[8]:


class s:
    data=[]
    def a(x):
        pn=int(input('enter inputs '))
        for i in range(pn):
            x.name=input('enter input name ')
            s.data.append(x.name)
            x.price=int(input('enter input price '))
            s.data.append(x.price)
    def dis(x):
        print('name ',x.name)
        print('price ',x.price)
        print( s.data)
                


# In[10]:


y=s()
y.a()
y.dis()


# In[14]:


class a:
    def p(self,enroll,name):
        self.e=enroll
        self.n=name
        nm=self.n[:2]
        en=self.e[:4]
        self.password=nm+en
        print(self.password)
    def login(self):
        password=self.password
        uid=int(input('enter enrollno: '))
        upass=input('enter password: ')
        if upass==password:
            print('login sucess')
        else:
             print('login fail')


# In[15]:


x=a()
x.p('2300217','abcde')
x.login()

