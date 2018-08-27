
# coding: utf-8

# In[1]:


MyFirstList = [3,6,165,13,6]


# In[2]:


MyFirstList


# In[3]:


type(MyFirstList)


# In[4]:


l2=["hello",24,True,44.75]


# In[5]:


l2


# In[6]:


l3 = ["how are you", 55, MyFirstList]


# In[7]:


l3


# In[8]:


#---


# In[9]:


range(15) #in Python 3. In Python 2 it was known as xrange()


# In[10]:


list(range(15))


# In[11]:


x = [1,2,3,4,5,6,7]


# In[12]:


x


# In[13]:


y = list(range(8))


# In[14]:


y


# In[15]:


z = list(range(1,8))


# In[16]:


z


# In[17]:


z2=list(range(100,120))


# In[18]:


z2


# In[19]:


w = list(range(100,111,2)) # zakres z jakiego chcemy liczby, trzecia pozycja mówi co ile (step of the number iteration)


# In[20]:


w


# In[21]:


w2 = list(range(100,201,10))


# In[22]:


w2


# ---

# In[23]:


w = ['a', 'b', 'c', 'd', 'e']


# In[24]:


w


# In[25]:


w[0] # gives us an element with index 0


# In[26]:


len(w) #lenght of list


# In[27]:


w[4]


# In[28]:


w


# In[29]:


# 0    1    2    3    4 


# In[30]:


# -5  -4   -3   -2   -1 #negative indexation method


# In[31]:


w[-1] # different behaviour than R - it would exclude the first (1) element and then give rest of the vector


# In[32]:


w[-3]


# In[33]:


w[2]


# In[34]:


# overwrite values:


# In[35]:


w


# In[36]:


w[2] = 63


# In[37]:


w


# In[38]:


w[10]=55


# In[39]:


l3


# In[40]:


l3[1]


# In[41]:


l3[2]


# In[42]:


l3[4]


# In[43]:


l3[2[1]]


# In[44]:


l3


# In[45]:


MyFirstList


# In[46]:


MyFirstList[2] = "surprise"


# In[47]:


l3


# In[48]:


l4 = l3


# In[49]:


l4


# In[50]:


len(l4)


# In[51]:


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J']


# In[52]:


letters


# In[53]:


letters[:] # colon (:) it's from slicing, but here is nothing on left and right, so we get whole list


# In[54]:


letters[2:] #here it slices from 2 to the very end


# In[55]:


letters[:7]


# In[56]:


letters[2:7]


# In[57]:


letters[-8:7] # here on the left we used negative indexation


# In[58]:


letters[-8:-3]


# In[59]:


#--- Advanced slicing


# In[60]:


letters[2:9] 


# In[61]:


letters[2:9:2] #slices from 2 to 9 and gets elements with step of 2


# In[62]:


letters[::3] #gets elements with step of 3


# In[63]:


letters[::-1]


# In[64]:


letters[2:9:-2] #if the slice has got positive indexation, step must also be positive or reverse first 2 numbers (shown later)


# In[65]:


letters[-2:-9:-2]


# In[66]:


letters[2:9:1]


# In[67]:


letters[-2:-9:1] #if the slice has got negative indexation, step must also be positive or reverse first 2 numbers (shown later)


# ----

# In[68]:


letters[::-1]


# In[69]:


letters[2:7]


# In[70]:


letters[2:7:-1]


# In[71]:


letters[6:1:-1] #to jest odwrotny efekt do kodu wyżej letters[2:7] - reversed effect


# In[72]:


letters


# In[73]:


letters[6:1:-2]


# ----

# In[74]:


#tuple = immutable list


# In[75]:


t1 = (345,763,826)


# In[76]:


t1


# In[77]:


t1[0]


# In[78]:


#What's the difference between tuple and list? Any element in tuple can't be changed!
t1[0] = 45
#  'tuple' object does not support item assignment

