#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Write a Python class to implement pow(x, n).


class find_power:

    x = int(input())
    n = int(input())   

    def __init__(self,x,n):
        self.x=x
        self.n=n
        
    def pow_num(self):
        result = x**n
        return result


power = find_power(x,n)
num=power.pow_num()
print(num)


# In[ ]:




