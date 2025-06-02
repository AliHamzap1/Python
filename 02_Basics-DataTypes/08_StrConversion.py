from datetime import datetime       # Import dattime for current_year

# Type Conversion
print("How to convert string to int, and int to string")

print("Convert str to int")
a = str(100)
print("Convert int to str")
b = int(a)

c = type(b)
print(c)



# Exercise
birth_year = input("Which year you born?\n")        #return string
current_year = datetime.now().year                  # Get current year as an integer
age = current_year - int(birth_year)                # Convert string to int

print(f"Your age is {age} years.")