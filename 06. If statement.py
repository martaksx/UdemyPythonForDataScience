
# coding: utf-8

# In[1]:


#---- -2 ---- -1 ---- 0 ---- 1 ---- 2


# In[2]:


import numpy as np


# In[3]:


from numpy.random import randn


# In[4]:


randn() #press control enter instead of shift enter if you don't want to move down


# In[5]:


#---- -2 ---- -1 ---- 0 ---- 1 ---- 2
answer = None #if you don't put thios none, after running code can stay "leftover" from the previous code run
x = randn()
if x>1:
    answer = "Greater than 1"
print(x)
print(answer)


# In[6]:


#---- -2 ---- -1 ---- 0 ---- 1 ---- 2
answer = None #if you don't put thios none, after running code can stay "leftover" from the previous code run
x = randn()
if x>1:
    answer = "Greater than 1"
else:
    answer = "Less than 1"
print(x)
print(answer)


# In[7]:


#---- -2 ---- -1 ---- 0 ---- 1 ---- 2
# Nested statements
answer = None
x = randn()
if x>1:
    answer = "Greater than 1"
else:
    if x>= -1:
        answer = "Between - 1 and 1"
    else:
        answer = "Less than -1"
print(x)
print(answer)


# In[8]:


#---- -2 ---- -1 ---- 0 ---- 1 ---- 2
# Chained statements
answer = None
x = randn()
if x>1:
    answer = "Greater than 1"
elif x>= -1:
    answer = "Between - 1 and 1"
else:
    answer = "Less than -1"
print(x)
print(answer)


# In[9]:


#---- -2 ---- -1 ---- 0 ---- 1 ---- 2
# Chained statements
answer = None
x = randn()
if x>1:
    answer = "Greater than 1"
elif x>= -1:
    answer = "Between - 1 and 1"
else:
    answer = "Less than -1"
    print("Hello")
print(x)
print(answer)

