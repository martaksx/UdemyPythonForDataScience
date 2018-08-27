
# coding: utf-8

# In[1]:


#Boolean / logical values:


# In[2]:


#True


# In[3]:


#False


# In[4]:


4<5


# In[5]:


10>100


# In[6]:


4 == 5


# In[7]:


# == equals
# != or <>
# <
# >
# <=
# >=
# and (in R its &)
# or (in R its /)
# not


# ---

# In[8]:


result=4<5


# In[9]:


result


# In[10]:


type(result)


# In[11]:


result2 = not(5>1)


# In[12]:


result2


# In[13]:


result or result2 #checks, if at least one element is true


# In[14]:


result and result2 #here all elements have to be true to make this true


# In[15]:


result3=4!=4
result3


# In[16]:


result4=4!=5
result4


# In[17]:


print(result)
print(result2)
print(result3)
print(result4)


# In[18]:


result and result4


# In[19]:


result2 and result3


# In[20]:


result or result2


# In[21]:


result3 or result4


# In[22]:


(result or result2) and (result3 or result4)


# In[23]:


result or result2 and result3 or result4

