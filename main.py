# This is a python cheatsheet

#Data types
int = 5
float = 5.0
str = "I went to the store"
Bool = True or False

# Lists
#List of groceries to buy
groceries = ["Pepper, Apple, Orange"]
#methods can be applied to lists:
groceries.append("Jake") # Add item to end of list
groceries.count() #Count items in the list with specified value, if there one item given as characters in word
groceries.clear() # Clears all elements from list
groceries.copy() # Returns a copy of the list
groceries.extend() # Add elements of any iterable(list, dictionaries, string) to current list
groceries.index() # Returns the index with the first item with the specified value
groceries.remove() #  Removes the first item with the specified value
groceries.reverse() #  Reverses list order
groceries.order() # Sorts the list in aplhanumerical order - does capital letters first

# Dictionaries

# Functions
# When creating a function we must define it like so:
def calculate(number):
    print(number + 2)

calculate(5)
# Will print 7
