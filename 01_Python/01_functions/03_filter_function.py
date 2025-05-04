# Filter Function in Python is a built-in function that takes in a function and a list as arguments.

# This function is called with all the items in the list and a new list is returned which contains items for which the function returns True

# Here we take function and list as arguments , then filter the data of the list and return the new list according to the function/requirement/




def even(num):
    if num % 2 == 0:
        return True


ele = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result =  list(filter(even, ele))
print(result)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x > 5 , num))
print(result)

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0 and x > 5 , num1))
print(result)