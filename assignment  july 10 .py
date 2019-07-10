#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
def reverseFib(n):
    a = [0] * n 
    a[0] = 0 
    a[1] = 1 
    for i in range(2, n):  
        a[i] = a[i - 2] + a[i - 1] 
    for i in range(n - 1, -1 , -1):  
        print(a[i],end=" ") 
        
n = 5 
reverseFib(n)


# In[ ]:


#10
def seriesGen2(n):
   i=1
   while i<=n:
       print(i,end="  ")
       i=i*2
   return
seriesGen2(100)


# In[ ]:



# term of geometric progression  
import math  
 
def Nth_of_GP(a, r, N):  
   return( a * (int)(math.pow(r, N - 1)) )  
a = 2
r = 3 
N = 5   
print("The", N, "th term of the series is :",  
                           Nth_of_GP(a, r, N))


# In[ ]:


# Series Generation

def seriesgeneration(n):
   i=1
   while i<=n:
       print(i,end=" ")
       i=i*3
   return
seriesgeneration(100)


# In[4]:


#2Q
def Q2(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
    for j in range(n):
        if i!=j:
            if a[i]==a[j]:
                c+=1
    if c==0:
        s=s+a[i]
    return s
Q2(int(input("no of values")))


# In[1]:


def Q3(a,b):
    if len(a)<=len(b):
        n=len(a)
        k=len(b)
    else:
        n=len(b)
        k=len(a)
    for i in range(n):
        print(a[i],b[i])
    for j in range(n,k):
        if(len(a)<=len(b)):
            print(b[j],'*')
        else:
            print(a[j],'*')
    return
x=str(input("enter str:"))
x=x.split()
Q3(x[0],x[1])


# In[10]:


def Q4(a,b):
    if len(a)>=len(b):
        print(a.upper())
    else:
        print(b.upper())
    return
x=str(input("enter str:"))
x=x.split()
Q4(x[0],x[1])


# In[18]:


def Q5_1(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
x=str(input("enter str:"))
Q5_1(x)


# In[16]:


def Q7(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
Q7(list(x))


# In[ ]:




