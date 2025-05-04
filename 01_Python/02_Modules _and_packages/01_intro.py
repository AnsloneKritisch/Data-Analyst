# MOdules and packages in Python 
# helps to organise and reuse code in Python

# there are 2 types of modules in Python
# 1. Built-in modules - are of 2 types
# 1.1 Standard modules - already included in Python by default
# 1.2 Third-party modules - not included in Python by default 
# 2. Custom modules

# Built-in modules in Python - standard modules - math module
# To use all the functions in math module we need to import it
import math
square_root = math.sqrt(25)
print(square_root)

# Built-in modules in Python - Third-party modules - numpy module
# we can't directly import numpy module and use it as it is not included in Python by default
# we need to install numpy module using pip install numpy

import numpy
array = numpy.array([1, 2, 3, 4, 5])
print(array)

#  we can also use alias while importing the module
# mostly you can just use numpy as np instead of writing numpy every time

import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array)

# Wher you write import modules get import but not all so -
# to import all the functions in numpy module we need to use *
from math import *
print(sqrt(25))


# 2. Custom modules
# we can create our own modules and import them
# to create a module we need to create a file with .py extension
# to import a module we need to import it using import keyword

from packages.math import add

print(add(1, 2))

# as you know we have 2 function in my module add and sub

from packages.math import *

print(add(1, 2))
print(sub(4, 2))

# now after adding a subpackage in our package

from packages.subpackages.multiply import multi

print(multi(2, 3))