
# coding: utf-8

# In[1]:


A = 10


# In[2]:


B=5


# In[3]:


#Arithmetics


# In[4]:


C = A+B


# In[5]:


C


# In[6]:


D=B/A


# In[7]:


D


# ---

# In[8]:


#Printing


# In[9]:


C


# In[10]:


print(C) #Print here is different than in Python  2.7 (there was without () )


# In[11]:


print(D) #division is different to Python 2.7 (there integer/integer would be cutting decimal and make 0 here)


# In[12]:


#Why is it better to use print() ?


# In[13]:


C
D


# In[14]:


print(C)
print(D)


# ---

# In[15]:


import math #importing modeule math


# In[16]:


math.sqrt(144)


# In[17]:


math.sqrt(A)


# In[18]:


round(math.sqrt(A))


# ---

# In[19]:


greeting="Hello"
name = "Marta"


# In[20]:


message = greeting + " " + name


# In[21]:


print(message)


# In[22]:


message2 = greeting + " "+name + " you have number" + " " + str(A)


# In[23]:


print(message2)


# In[24]:


message3 = greeting + " "+name + " you have number" + " " + str(2.55)


# In[25]:


print(message3)

