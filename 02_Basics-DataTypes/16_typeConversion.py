from datetime import datetime


# Create a program that Guess your age

birth_year = input('What year were you born?')
# Find Current Year
current_year = datetime.now().strftime('%Y')

# Test Data Types
# print(type(birth_year))     # <class 'str'>
# print(type(current_year))   # <class 'str'>

age = int(current_year) - int(birth_year)
# print("Your age is " + age + ".") # Basic way of Str Concatination
print(f"Your age is {age}.")