
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn
N = 1000                                   #specify sample size
counter = 0                               #reset counter
for i in randn(N):                        #iterate over random values
    if (randn() >=-1 and randn()<=1 ):    #check where iterated variables falls
        counter = counter + 1             #increase counter if condition is met
answer = counter/N                        #calculate hit-ratio
print(answer)                             #print answer

