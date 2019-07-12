#!/usr/bin/env python
# coding: utf-8

# ### regular expression
# - pattern matching
# - patterns(re) package
# - Cap symbol is used to represent the start of re
# - Dollor symbol is used to represent the end of re
# - [0-9]-->any digit matching
# - two digit number (^[0-9]{2}$)-Five Digit number(^[0-9]{5}$)
# 

# ### Regular Expression for characters
# - [a-z]--> Any lower case characters
# - [A-Z]--> Any upper case characters
# - ^[a-z]{5}$--> It aacept 5 lower case characters
# - ^[a-zA-Z]{8}$--> Accept 8 characters can be anything lower and upper
# - ^[a-zA-Z0-9]{8}$--> Accept 8 characters can be anything lower,upper and digit

# In[2]:



#Fuction to test two digit number matching
import re
def twoDigitMatching(n):
    pattern='^[0-9]{2}$'
    n=str(n)
    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(12)) #True
print(twoDigitMatching(123)) #False


# In[3]:


#Function to define to test username having 8 characters
#Upper case and lower
def testUsername(s):
    pattern='^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))


# ### Regular Expression to match the India Mobile Number
# - 10 Digits
# - (First digit will be [6-9]) and remaining 9 digits will be [0-9]
# - Example:- 9535152553
# - Re- ^[6-9][0-9]{9}$
# - Example:- 09988774455

# In[6]:


#Function to validate the Indian Mobile number 
def phoneNumberValidation(phone):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
phoneNumberValidation('+919988774455')


# - Regular Expression to Validate the RollNumber
# - Example : 1521A0501
# - Example : 1521A0109
# - Example : 1521A0499
# - Regular Expression to validate the password
# - Parameters: Len min of 6 characters and Max of 15 characters
# - Accept Lower case,Upper case,Digits Spl char(@,#,!)

# ### Email Id validation using Regular Expression
# - Example:- Username@DomainName.extension
# - Username:- 
# - Length will be [6-15]
# - No Spls characters apart from Underscore(_)
# - Should not begin and ends with Underscore(_)
# - Characters Set: All digits and lower case
# - DomainName:-
# - Length will be [3-18]
# - No spls characters 
# - Character Set: All digits and lower case
# - Extension:-
# - Length will be [2-4]
# - No Spl characters
# - Character Set: Lower case Characters

# In[10]:


def emailValidation(email):
    pattern='^[0-9a-z][0-9a-z_.]{5,14}[@][a-z0-9]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
emailValidation('rishikamallipeddi@gmail.com')


# ### Python Turtle
# - Turtle Graphics

# In[ ]:


#Step1: Make all the turtle package to be imported
import turtle
#Turtle method creates and returns a new object
a1=turtle.Turtle()
#forward() method moves 100 pixels
turtle.forward(250)
#we are done 
turtle.done()


# In[ ]:



#Line draw in reverse direction
import turtle as tt
a1 = tt.Turtle
tt.backward(100)
tt.done()


# In[ ]:



#Draw a square
import turtle as tt
a1=tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[ ]:


#Loop statement
import turtle as t
aa=t.Turtle()
for i in range(4):
    aa.backward(150)
    aa.left(90)
t.done()


# In[ ]:



# Star
import turtle as t
a1 = t.Turtle()
for i in range(40):
   a1.forward(50)
   a1.right(144)
t.done()


# In[ ]:


# Spiraling Star
import turtle as t
a1 = t.Turtle()
a1.pencolor('blue')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[ ]:


# Square Spiral help of Turtle
import turtle as t
a1 = t.Turtle()
for i in range(250):
    a1.forward(i)
    a1.left(91)
t.done()   


# In[1]:


# Hexagon with Multi Color
from turtle import*
colors = ['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)


# In[2]:



# goto function

from turtle import*
goto(50,50)
goto(-50,50)
goto(100,-50)
goto(-50,-50)


# In[3]:



#setheading(heading)
#will change the current direction to the heading angle
from turtle import*
colors=['blue','red','purple','orange','green','yellow']
for angle in range(0,360,15):
    pencolor(colors[angle%6])
    setheading(angle)
    forward(100)
    write(str(angle)+'o')
    backward(100)



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




