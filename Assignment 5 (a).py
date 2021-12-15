#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Write a Python class to implement pow(x, n).

class find_pow:
    def power(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.power(x,-n)
        val = self.power(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

x=int(input("Enter x value :"))
n=int(input("Enter n value :"))

obj_pow=find_pow().power(x,n)
print("pow(x,n) value is :",obj_pow)


# In[ ]:




