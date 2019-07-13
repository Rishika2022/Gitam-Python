#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle 

turtle.color("green")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()
turtle.color("orange")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()


# In[ ]:



import turtle 

turtle.color("green")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()
turtle.color("orange")
turtle.begin_fill()
turtle.circle(130,180)
turtle.end_fill()
turtle.hideturtle()


# In[ ]:


#Draw a Spirling Square with Pen color as 'Red'
import turtle as y
a=y.Turtle()
a.pencolor('red')
for i in range (100):
    a.forward(i)
    a.left(91)
y.done()


# In[14]:


def printLarge(n):
    large = 0
    while n != 0:
        r = n % 10
        if large < r:
            large = r
        n = n // 10
    return large
printLarge(195263)


# In[1]:


def isPalindrome(n):
    rev = 0
    buffer = n
    while n!= 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if rev == buffer:
        return True
    else:
        return False
    return


# In[7]:


def countPalindrome(lb,ub):
    cnt = 0
    while lb != ub:
        # Implement
        if isPalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countPalindrome(1,10)


# In[2]:



#5. Write a python programming to create and find the word count from given input file
def wordcount(filename,word):
    with open(filename,'r') as f:
        if f.mode =='r':
            x=f.read()
        li= x.split() 
        cnt=li.count(word)
        return cnt
filename = input('enter the file name : ')
word=input('enter the word : ') 
wordcount(filename,word)


# In[2]:



#  5
def createfile(filename):
    f=open(filename,'w')
    for i in range(10):
         f.write('This is %d line\n'%i)
    print("file is created and data has written")
    return
createfile('file1.txt')


# In[ ]:





# In[ ]:





# In[ ]:




