# Exception handling in Python
# Error handling in Python
# Python gives error when we write wrong code but we sometimes can't handle the error
# SO we use try and except block to handle the error

try :
    result = 10 / 0

except ZeroDivisionError as e:
    print(e)
    print("You can't divide a number by zero")


# let's have thoro use of try except block

# try is basically used to handle the function and except is used to handle the error
# here we write the condition i want to try 
try :
    num = int(input("Enter a number : "))
    result = 10 / num

except ZeroDivisionError as e:
    print(e)
    print("You can't divide a number by zero")

except ValueError as e:
    print(e)
    print("Invalid input")

else:
    print(result)

finally:
    print("This will always execute")
    
