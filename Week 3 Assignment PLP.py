#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price: The original price of the item.
    - discount_percent: The discount percentage to be applied.
    
    Returns:
    - The final price after the discount if the discount is 20% or higher.
    - The original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompting the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculating the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Printing the final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")


# In[ ]:




