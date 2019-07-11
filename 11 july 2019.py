#!/usr/bin/env python
# coding: utf-8

# # Standard Libraries
# - File I/O
# - Regular Expression
# - Datetime
# - Math(numerical and Mathematical)

# ### File Handling in Python
# - File:- Document containing information resides on the permanent storage
# - Different types of files:-txt,doc,pdf,csv and etc..
# - Input -- Keyboard
# - Output -- File

# ## Modes of the File I/O
# - 'w'--This mode is used to file writing
# - -- If the file is not present first it creates the file and write so me data to it
# - -- If the File is already present then it will rewrite the previous content

# In[2]:


#Function to create a file and write to the file
def createFile(filename):
   f=open(filename,'w')
   for i in range(10):
       f.write('This is %d Line'%i)
   print("File is created and data has written")
   return
createFile('file1.txt')


# In[4]:


ls


# In[6]:


def createFile(filename):
   f=open(filename,'w')
   f.write('Testing..\n')
   print("File is created and data has written")
   return
createFile('file1.txt')


# In[8]:


def appendData(filename):
   f=open(filename,'a')
   for i in range(10):
       f.write("This is %d Line\n"%i)
   print("FileCreated and Successfully data written")
   return
appendData('file2.txt')


# In[5]:



def appendData(filename):
   f=open(filename,'a')
   f.write("New Line1\n")
   f.write("New Line2\n")
   print("FileCreated and Successfully data written")
   return
appendData('file2.txt')


# In[9]:


#Function to read of the file
def readFileData(filename):
    f=open(filename,'r')
    if f.mode=='r':
        x=f.read()
        print(x)
    f.close() 
    return
readFileData('file2.txt')


# In[7]:


#Function to read the File
def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode=='r':
            data=f.read()
            print(data)
        elif f.mode=='a':
            f.write('Data to the File')
            print('The data successfully written')
    f.close()
    return
filename=input('Enter the file name')
mode=input('Enter the mode of the file')
fileoperations(filename,mode)


# In[2]:



#Data Analysis
#Word Count Program
def wordCount(filename,word):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=x.split() # It's splits the string with whitespace
    cnt=li.count(word)
    return cnt
filename=input('Enter the file name: ')
word=input('Enter the word: ') # which word count you need
wordCount(filename,word)


# In[3]:


#character count from the given file
def charCount(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    return len(li)
filename=input('Enter the filename:')
charCount(filename)


# In[4]:



s1="Python Programming"
print(s1.split('a'))


# In[5]:


#Function to find the no of lines in the input file
#Input--filename(file2.txt)
#output--No of lines(12)
def countOfLines(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=x.split("\n")
    return len(li)
filename=input('Enter the filename :')
countOfLines(filename)



# In[6]:



#Function to print the Upper and Lower characters
def caseCount(filename):
    cntUpper=0
    cntLower=0
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    for i in li:
        if i.isupper():
            cntUpper+=1 #cntUpper=cntUpper+1
        elif i.islower():
            cntLower+=1 #cntLower=cntLower+1
    output='Upper Case={0},Lower Case={1}'.format(cntUpper,cntLower)
    return output
filename=input('Enter the filename :')
caseCount(filename)


# ## math,random,os
# - os package it contains the certains methods which works with OS
# 

# In[7]:


ls


# In[8]:


cd desktop/pythonprog/git


# In[9]:


cd


# In[15]:


import os
os.listdir('Git/')


#  ## Listing all files in a Dictionary

# In[17]:


import os
dirPath="Git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# In[18]:


import os
dirPath="Git/"
for i in os.listdir(dirPath):
   if os.path.isfile(os.path.join(dirPath,i)):
       print(i)


# ##  filename pattern matching

# In[20]:


cd..


# In[21]:


import os
dirpath='git/'
for f_name in os.listdir(dirpath):
    if f_name.endswitch('05'):
        print(f_name)


# ## deleting files and directories

# In[22]:


li=os.scandir('git/')
for i in li:
   print(i)


# In[23]:


from pathlib import Path
li=Path('git/')
for i in li.iterdir():
   print(i.name)


# In[24]:


Listing SubDirectories
In [34]:
dirPath='git/'
for i in os.listdir(dirPath):
if os.path.isdir(os.path.join(dirPath,i)):
print(i)


# In[25]:



from pathlib import Path
dirPath=Path('git/')
for i in dirPath.iterdir():
   if i.is_dir():
       print(i.name)


# In[26]:



   Creating a Single Directory
In [61]:
import os
os.mkdir('single directory')
import pathlib
p=pathlib.Path('TestFolder')
p.mkdir()
   Creating Multiple Directory
In [60]:
import os
os.makedirs('2019/july/11/Thursday')





# In[ ]:



import os
dirPath='git/'
for f_name in os.listdir(dirPath):
   if f_name.endswith('ipynb'):
       print(f_name)


# In[27]:


import os
dirPath='git/'
for f_name in os.listdir(dirPath):
   if f_name.startswith('ipynb'):
       print(f_name)


# In[ ]:



import os
data_file="single directory"# give the entire path
os.rmdir(data_file)


# In[ ]:


import shutil # delete the tree of structure of folder
data_dir='2019'
shutil.rmtree(data_dir)
ls


# In[ ]:





# In[ ]:




