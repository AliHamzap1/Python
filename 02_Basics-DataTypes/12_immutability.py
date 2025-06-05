# Immutability

# Immutability refers to the property of an object that prevents it from being modified after it has been created.
# In Python, immutable objects include:
# - Integers
# - Floats
# - Strings
# - Tuples
# Mutable objects, on the other hand, can be modified after creation. Examples include:
# - Lists
# - Dictionaries
# - Sets



# Strings are immutable, so we cannot change them directly.
immutable_string = "Hello, World!"
# Attempting to change a character in the string will raise an error
try:
    immutable_string[0] = 'h'  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")


# However, we can create a new string based on the original
new_string = 'h' + immutable_string[1:]  # Create a new string with the first character changed
print(new_string)  # Output: "hello, World!"
