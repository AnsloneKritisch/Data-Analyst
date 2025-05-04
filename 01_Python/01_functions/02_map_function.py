
# The map() function in Python takes in a function and a list as arguments.
# This function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

# Example of using the map() function in Python
def square(num):
    return num ** 2

nums = [1, 2, 3, 4, 5]

# takes two argument her one function and second list then apply the fuction in all the list element and return the new list
result = list(map(square, nums))
print(result)  # Output: [1, 4, 9, 16, 25]


# Example 2 of using the map() function and lamda function in Python

nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, nums))
print(result)

# Example 3 of using the map() function and lamda function in Python
words = ['apple', 'banana', 'cherry']
result = list(map(lambda x: x.upper(), words))
print(result)
