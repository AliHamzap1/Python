# Fundamental Data Types

# There are some different data types
int
float
str
complex 
# complex number is a number that can be expressed in the form a + bi, where a and b are real numbers, and i is the imaginary unit, which satisfies the equation i² = -1.
bool
list
tuple
set
dict
None # it is also a data type
# "None" is use for "Nothing" in other Programming languages user known it as "NULL".

# Classes -> custom types (data types)
# Like Car, Object etc

# Specialized Data Types (Libraries and extensions etc):
# These are modules of a Language, Means when any type of work which can not be done by classes or methods when we use Extensions or libraries, 
# This process is called Modules.

# Data Types:

# Primitive/Fundamental data type: 
# Each variable in any programming language has an associated data type. Each data type requires different amounts of memory and has some specific operations which can be performed over it. (eg: int, float, char, double, etc.).

# Derived data type : 
# These data types are defined by user itself. Like, defining a class in C++ or a structure. These include Arrays, Structures, Class, Union, Enumeration, Pointers etc. 

# Find the type of the value
type(9 + 1) # int
type(9.1 + 1.9) # float beacuse result is 11.0
type(1)   # int
type(-10) # int
type(0)   # int
type(0.0) # float
type(2.2) # float
type(4E2) # float - 4*10 to the power of 2


# Airthmetic Operators (Math Function):

10 + 3  # 13
10 - 3  # 7
10 * 3  # 30
# n ** n, this means n is the power of n
10 ** 3 # 1000
10 / 3  # 3.3333333333333335
# This Round off the result of Division
10 // 3 # 3 --> floor division - no decimals and returns an int
# This Return the remainder of division value
10 % 3  # 1 --> modulo operator - return the remainder. Good for deciding if number is even or odd


# Basic Functions:

print(pow(5, 2))
pow(5, 2)      # 25 --> like doing 5**2
# Absolute value means No Negative Numbers
abs(-50)       # 50
# To round any value
round(5.46)    # 5
round(5.468, 2)# 5.47 --> round to nth digit
bin(512)       # '0b1000000000' -->  binary format
hex(512)       # '0x200' --> hexadecimal format


# Functions in Python Math Module "Online Link"
# https://docs.python.org/3/library/math.html
# https://www.programiz.com/python-programming/modules/math
