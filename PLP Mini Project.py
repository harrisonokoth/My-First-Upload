#!/usr/bin/env python
# coding: utf-8

# Mini Project
# 
# In this project, you are tasked to create a program that automates searching for a word definition in a dictionary. Follow the instructions to implement
# 
# Dictionary Project is provided here: https://github.com/mutemip/dictionary-data
# 
# We should have a data source (Download from the link above)
# Learn how to load json data into a python dictionary
# Create a function that returns a definition of a word
# Consider a condition that the entered word is not in a dictionary
# Consider input from user having different cases – upper/ lower case or mixed eg: RAIN/rain/RaIN
# Make your dictionary program more intelligent incase users input a word with wrong spelling the program should be able to suggest the word that might be intended.
# eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here

# In[14]:


import json
import difflib

# Loading the JSON data into a Python dictionary
def load_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
        return None

# Function to get the definition of a word
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        suggestions = difflib.get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)
        if suggestions:
            return f"Did you mean '{suggestions[0]}'? Definition: {dictionary[suggestions[0]]}"
        else:
            return "The word does not exist in the dictionary."

# Main function to run the dictionary program
def main():
    # Loading the dictionary data
    file_path = "D:/Documents/data.json"
    dictionary = load_dictionary(file_path)
    if not dictionary:
        return
    
    # Geting input from the user
    word = input("Enter a word to get its definition: ").strip()
    
    # Geting and printing the definition
    definition = get_definition(word, dictionary)
    print(definition)

if __name__ == "__main__":
    main()


# Explanation:
# Loading JSON Data:
# 
# The load_dictionary function reads the JSON data from the specified file path and loads it into a Python dictionary.
# Getting the Definition:
# 
# The get_definition function takes a word and the dictionary as input.
# It converts the word to lowercase to handle different cases.
# If the word is found in the dictionary, it returns the definition.
# If the word is not found, it uses difflib.get_close_matches to suggest the closest matching word if there is one.
# Main Function:
# 
# The main function loads the dictionary, prompts the user to enter a word, and then prints the definition or a suggestion if the word is misspelled.
# Error Handling:
# The program includes error handling for file not found and JSON decoding errors.
