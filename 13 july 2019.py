#!/usr/bin/env python
# coding: utf-8

# ### Tranforming Code into Idiomatic Python
# - Replace traditional index manupulation with Python core looping idiomatic
# 

# In[1]:



#Idiomatic Programming
for i in range(6):
   print(i**2,end=" ")


# 
# ### Looping Over a Collection

# In[2]:


colors=['red','green','yellow','purple']
for i in range(len(colors)):
   print(colors[i],end=" ")


# In[3]:



for color in colors:
   print(color,end=" ")


# In[4]:


colors=['red','green','yellow','purple']
for i in range(len(colors)-1,-1,-1):
   print(colors[i],end=" ")


# In[5]:



for color in reversed(colors):
   print(color,end=" ")


# 
# ###
# - if x<=y and y<=z:
# - if x<=y<=z:
# - if x==True:
# - if x:

# ### Pandas
# 

# In[2]:


import pandas as pd


# In[3]:


dt={'Id':[11,12,13,14,15],
  'first_name':['A','B','C','D','E'],
  'company':['aa','bb','cc','dd','ee'],
  'address':['Hyd','Hyd','Hyd','Hyd','Hyd']}
mydt=pd.DataFrame(dt)


# In[4]:


print(mydt)


# In[5]:


import os


# In[1]:


Reading the data from CSV file
mydata=pd.read_csv('workingFile.csv')


# In[7]:


print(mydata)
os.chdir("D:\\MyData\\")# Saves to certian location


# In[2]:



mydt.to_csv('WorkingFile.csv',index=False)


# ##  Reading the data from CSV file
# 

# In[1]:


mydata=pd.read_csv('workingFile.csv')


# In[2]:



print(mydata)
os.chdir("D:\\MyData\\")# Saves to certian location


# In[2]:



mydt.to_csv('WorkingFile.csv',index=False)


# In[3]:


mydata1=pd.read_csv('WorkingFile.csv',skiprows=1,
                   names=["CustId","Name","Company","Address"])


# In[ ]:



print(mydata1)

