#!/usr/bin/env python
# coding: utf-8

# In[54]:


# Homework #3, Nathan McCall
#
#
# Imports
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
#One thousand values from 0 to 2*pi using linspace
x = np.linspace(0, 2 * np.pi, 1000)
#Functions
w = 5.5*np.cos(2*x)+5.5
y = 0.02*np.exp(x)
z = 0.25*x**2 + 0.1*np.sin(10*x)
#Axis labels
plt.xlabel('Time in ASTR 119')
plt.ylabel('Measure of Awesomeness')
#X and Y axis Limits
plt.xlim([0,2*np.pi])
plt.ylim([-1,10])
#Plot Functions and Show them on Graph
plt.plot(x,w)
plt.plot(x,y)
plt.plot(x,z)
plt.show()


# In[ ]:


#y(x) = 5.5 cos(2 * x) + 5.5

#y(x) = 0.02 * exp( x )

#y(x) = 0.25 * x^2 + 0.1 sin (10 * x)

