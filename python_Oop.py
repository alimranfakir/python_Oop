#!/usr/bin/env python
# coding: utf-8

# In[1]:


#class

class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

r = Resistor('10-232-1412', 'honhai', 10)
print(f'{r.__dict__ = }')


# In[2]:


# lets look at the size of the object
# no need to define it again. I am just following him with running with current line
class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

from sys import getsizeof
print(f'{getsizeof(Resistor(None, None, None))} = ')


# In[ ]:




