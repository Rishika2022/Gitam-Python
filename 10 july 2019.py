#!/usr/bin/env python
# coding: utf-8

# ### Tuples
# - t1 parenthesis() li square brackets[]
# - difference between list and tuples
#      - list are mutable - can be changed / modified
#          - used to access modify,add,delete data
#   - tuples are immutable - vcannot be changed
#       - used to access data only

# In[18]:


t1 = (1,2,3,4,5,6)
t1
type(t1)


# # Data Structures
# 
# ### Dictionaries
# - it works on the concept of set unique data
# - each key is separated from its value with colon(:)
# - keys,values are the unique identifiers for a value
# - each key and value are separated by comma(,)
# - dictionaries enclosed with curly braces({})
# 

# In[4]:


d1={"name":"gitam","emailid":"gitam@gmail.com","address":"hyderabad"}
print(d1)


# In[6]:


d1["name"]


# In[8]:


d1['emailid'] = 'gitam-python@gmail.com'


# In[10]:


d1['emailid']


# In[12]:


del d1['emailid']


# In[13]:


d1 


# In[14]:


d1.keys()


# In[15]:


d1.values()


# In[16]:


d1.items()


# # Contact Application
# - add contact
# - search the contact
# - list all contacts
#     - name1:phone1
#     - name2:phone2
# - modify the contact
# - remove the contact
# - import the contact

# In[20]:


# add contact
contacts = {} # creating a dict object
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("conact is details are added")
    else:
        print("contact details are already exists")
    return
addcontact('Surya','123456789')
addcontact('Pandu','987654321')
addcontact('Jai','7418529633')


# In[22]:


# search for contact details
def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exists" % name)
    return
searchcontact('Surya')
searchcontact('Pandu')
searchcontact('Jai')


# In[23]:


# import some contacts
# merge the contact with existing one
def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts={'rishi':4546789123,'chichu':654987321}
importcontact(newcontacts)


# In[24]:


# delete a contact
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"delete successfully")
    else:
        print(name,"not exists")
    return
deletecontact('chichu')


# In[25]:


contacts


# In[26]:


# update the contact details
def deletecontact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,"update successfully")
    else:
        print(name,"not exists")
    return
deletecontact('Jai',7418529633)
deletecontact('chichu',654987321)


# ### Sring Functions
# - upper()--will convert the string into upper function
# - lower()--will convert the string into lower function

# In[28]:


s1='gitam'
print(s1.upper())
print(s1.lower())


# ### Boolean Function(true and false)
# - islower()--true if the string is lower case / false if not lower case
# - isupper()--true if string is in upper / false if not upper case

# In[29]:


s1='GITAM'
print(s1.islower())
print(s1.isupper())


# In[30]:


s2="Python Programming"
s3="python Programming"
print(s2.istitle())
print(s3.istitle())


# In[31]:


s2="Application1889"
s3="PythonProgramming"
print(s2.isalpha())
print(s3.isalpha())


# In[32]:


s1="1234"
s2="Application1234"
print(s1.isnumeric())
print(s2.isnumeric())


# In[33]:


s1=" "
s2="Py th on"
print(s1.isspace())
print(s2.isspace())


# # String Methods
# - join()-- Method will concatinates the two strings
# - split()-- split() returns the a list of strings separted by whitespace(no parameters are given)
# -  join()-- Method will concatinates the two strings
# - replace()-- replaces the specific word/character with new word/character

# In[34]:


s1='Python'
print(" ".join(s1))


# In[35]:


s2="Python Programming Easy to learn"
print(",".join(s2))


# In[36]:


li =['Python','Programming','Learn']
print(",".join(li))


# In[37]:


s2="Python Programming Easy to learn"
print(s2.split())


# In[38]:


s2="Python Programming Easy to learn"
li=s2.split()
print(li)
print(len(li))


# # Packing and Modules
# ## Packages:
# - A collection of Modules(Single Python file.py) and Subpackages
# -Module
# - A Single python file containing set functions
# - Packages-->Sub Packages-->Modules-->Function-->Statements

# In[39]:


#Import the externals packages to Python File
import math
math.floor(123.45)


# In[40]:



from math import factorial as fact
fact(5)


# In[41]:



#Function to generate N random numbers in given range 
import random
def randomNumbers(n,lb,ub):
   for i in range(0,n):
       print(random.randint(lb,ub),end=" ")
   return
randomNumbers(10,0,100)


# In[ ]:





# In[ ]:




