#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT SUMMARY:
# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.[50,60,70]
# Extend my_list with another list:
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

# In[ ]:


1. Creating an empty list called my_list.


# In[1]:


my_list = []


# 2. Appending the elements 10, 20, 30, 40 to my_list.

# In[2]:


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


# 3. Inserting the value 15 at the second position in the list.

# In[3]:


my_list.insert(1, 15)


# 4. Extending my_list with another list:[50,60,70]

# In[4]:


my_list.extend([50, 60, 70])


# 5. Removing the last element from my_list.

# In[5]:


my_list.pop()


# 6. Sorting my_list in ascending order.

# In[6]:


my_list.sort()


# 7. Finding and printing the index of the value 30 in my_list.

# In[7]:


index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")


# 8.Printing the final sorted list to see the result.

# In[8]:


print("The sorted list is:", my_list)


# In[ ]:





# In[ ]:




