#!/usr/bin/env python
# coding: utf-8

# In[89]:


my_dict = {chr(i): i for i in range(97, 97 + 26)}
print(my_dict)


# In[93]:


def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[ ]:




