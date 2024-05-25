#!/usr/bin/env python
# coding: utf-8

# Task 1: Program to Accept User Input to Create a List of Integers and Compute the Sum

# In[1]:


# Task 1: Create a list of integers from user input and compute the sum

# Prompting user to enter integers separated by spaces
user_input = input("Enter a list of integers separated by spaces: ")

# Splitting the input string into a list of strings
string_list = user_input.split()

# Converting each string in the list to an integer
int_list = [int(num) for num in string_list]

# Computing the sum of all integers in the list
total_sum = sum(int_list)

# Printing the sum
print(f"The sum of the integers is: {total_sum}")


# Task 2: Create a Tuple of Book Names and Print Each Using a For Loop

# In[2]:


# Task 2: Tuple of favorite books and print each book name on a separate line

# Tuple containing the names of five favorite books
favorite_books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice", "Moby-Dick")

# Printing each book name on a separate line using a for loop
for book in favorite_books:
    print(book)


# Task 3: Program to Store Information About a Person Using a Dictionary

# In[3]:


# Task 3: Store and print information about a person using a dictionary

# Initializing an empty dictionary to store information about a person
person_info = {}

# Asking user for input and store it in the dictionary
person_info["name"] = input("Enter your name: ")
person_info["age"] = input("Enter your age: ")
person_info["favorite_color"] = input("Enter your favorite color: ")

# Printing the dictionary to the console
print(person_info)


# Task 4: Program to Create Two Sets of Integers and Find Common Elements

# In[4]:


# Task 4: Create two sets of integers and find common elements

# Prompting the user to enter integers for the first set
set1_input = input("Enter integers for the first set, separated by spaces: ")

# Prompting user to enter integers for the second set
set2_input = input("Enter integers for the second set, separated by spaces: ")

# Converting input strings to sets of integers
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

# Creating a new set containing elements common to both sets
common_elements = set1 & set2

# Printing the new set
print(f"The common elements are: {common_elements}")


# Task 5: Program to Create a List of Words and Filter Words with Odd Number of Characters Using List Comprehension

# In[5]:


# Task 5: Filtering words with odd number of characters using list comprehension

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Using list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Printing the new list
print(f"Words with an odd number of characters: {odd_length_words}")


# In[ ]:




